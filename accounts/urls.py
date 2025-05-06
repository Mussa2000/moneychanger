from django.urls import path, include

from accounts.views.user import CustomLogoutView, KYCProfileCreateView, KYCProfileUpdateView
from . import views
from django.contrib.auth import views as auth_views
from . import views
from accounts.views import(
    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDetailView,
    UserDeleteView,
    register_user,
    reset_password
)


urlpatterns = [
    path("auth/", include("allauth.urls")),
    path('user/index/',UserListView.as_view(), name="user-index"), 
    path('user/create/', register_user, name="user-create"),  
    path('user/password-reset/', reset_password, name="reset-password"),  
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name="user-update"), 
    path('user/details/<int:pk>/', UserDetailView.as_view(), name="user-details"), 
    path('user/delete/<int:pk>/',UserDeleteView.as_view(), name="user-delete"), 
    path('user/logout/', CustomLogoutView.as_view(), name="custom-logout"),
    path('user/signup/', views.CustomSignupView.as_view(), name="custom-signup"),
    
    path('kyc-profile/create/', KYCProfileCreateView.as_view(), name="kyc-profile-create"),
    path('kyc-profile/update/<int:pk>/', KYCProfileUpdateView.as_view(), name="kyc-profile-update"),
    
]
