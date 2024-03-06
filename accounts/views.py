from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.views import PasswordResetView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import View, TemplateView


class ChangeUsernameView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "account/change_username.html"
    success_url = reverse_lazy(
        "dashboard-view"
    )  # Replace 'home' with your app's home URL name

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, self.template_name, {"user": user})

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        new_username = request.POST.get("new_username")

        if User.objects.filter(username=new_username).exists():
            messages.error(
                request, "Username already exists. Please choose a different username."
            )
            return redirect(
                "change-username-view", user_id=user_id
            )  # Replace 'change_username' with your app's change_username URL name

        user.username = new_username
        user.save()
        messages.success(
            request, f"Username has been changed successfully to {new_username}."
        )
        return redirect(reverse("dashboard-view"))



class ChangePasswordView(View):
    template_name = "account/change_password.html"

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        return render(request, self.template_name, context={"user": user})

    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            new_password = request.POST["new_password"]
            user.set_password(new_password)
            user.save()
            messages.success(request, f"Password changed successfully: {new_password}")
            return redirect(
                reverse("dashboard-view")
            )  # Replace 'profiles' with the appropriate URL name
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
        return render(request, self.template_name)


#Custom email reset 

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'account/password_reset_email.html'
    html_email_template_name = 'account/password_reset_email.html'

    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None):
        html_email = render_to_string(html_email_template_name, context)
        email_message = EmailMessage(
            subject_template_name,
            html_email,
            from_email,
            [to_email],
        )

        email_message.content_subtype = 'html'
        email_message.send()