from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from accounts.forms.user import CustomUserCreationForm
from accounts.models.user import CustomUser
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserListView(ListView):
    model = CustomUser
    template_name = 'registration/index.html'
    context_object_name = 'user'

class UserCreateView(CreateView):
    model = CustomUser
    template_name = 'registration/create.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('user-list')
    
class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'registration/details.html'
    context_object_name = 'users'   

# class UserUpdateView(UpdateView):
#     model = CustomUser
#     template_name = 'registration/update.html'
#     form_class = UserChangeForm
#     success_url = reverse_lazy('user-list')
    

class UserDeleteView(View):
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
        
class UserUpdateView(UpdateView):
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