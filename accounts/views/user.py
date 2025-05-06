from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from accounts.forms import KYCProfileForm
from accounts.forms.user import CustomUserCreationForm
from accounts.models.user import CustomUser, KYCProfile
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class UserListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    model = CustomUser
    template_name = 'registration/index.html'
    context_object_name = 'user'

class UserCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('account_login')
    model = CustomUser
    template_name = 'registration/create.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('user-list')
    
class UserDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('account_login')
    model = CustomUser
    template_name = 'registration/details.html'
    context_object_name = 'users'   

# class UserUpdateView(UpdateView):
#     model = CustomUser
#     template_name = 'registration/update.html'
#     form_class = UserChangeForm
#     success_url = reverse_lazy('user-list')
    

class UserDeleteView(LoginRequiredMixin, View):
    login_url = reverse_lazy('account_login')
    def get(self, request, **kwargs):
        obj = get_object_or_404( CustomUser, pk=kwargs.get('pk'))
        obj.delete()
        messages.success(request,f'{obj} deleted successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            

from django.shortcuts import render, redirect, get_object_or_404

def register_user(request):
        if request.method == "GET":
            return render(
                request, "registration/create.html",
                {"form": CustomUserCreationForm}
            )
        elif request.method == "POST":
            form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("User created successfully"))
            return redirect('user-index')
        else:
            messages.success(request, ("Something went wrong please try again"))
            return redirect('user-create')
        
class UserUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('account_login')
    model = CustomUser
    template_name = 'registration/update.html'
    form_class = CustomUserCreationForm
    success_message = "User updated successfully"

    def get_success_url(self):
        return reverse("user-index")

    def form_valid(self, form):
        username = form.cleaned_data['username']
        user = self.object
        print(user)
        if user.username != username and CustomUser.objects.exclude(pk=user.pk).filter(username=username).exists():
            form.add_error('username', 'A user with that username already exists.')
            return self.form_invalid(form)
        return super().form_valid(form)
    
def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('reset-password')

        try:
            user = CustomUser.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password reset successfully.')
            return redirect('account_login')
        except CustomUser.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('reset-password')
    else:
        return render(request, 'registration/reset.html')
    
class CustomLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect(reverse("account_login"))  # Replace 'login-view' with your app's login URL name
    
    
    


class KYCProfileCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('account_login')
    model = KYCProfile
    form_class = KYCProfileForm
    template_name = "kyc_profile/create.html"
    success_message = "KYC Profile created successfully"

    def dispatch(self, request, *args, **kwargs):
        if KYCProfile.objects.filter(user=self.request.user).exists():
            messages.info(request, "You already have a KYC Profile. You can update it instead.")
            return redirect(reverse("kyc-profile-update", kwargs={"pk": KYCProfile.objects.get(user=self.request.user).pk}))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("kyc-profile-create")


class KYCProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('account_login')
    model = KYCProfile
    form_class = KYCProfileForm
    template_name = "kyc_profile/update.html"
    success_message = "KYC Profile updated successfully"

    def get_queryset(self):
        return KYCProfile.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("kyc-profile-create")