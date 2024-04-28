from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from . import views
from accounts.views import(
    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDetailView,
    UserDeleteView,
    register_user
)


urlpatterns = [
    path("", include("allauth.urls")),
    path('user/index/',UserListView.as_view(), name="user-index"), 
    path('user/create/', register_user, name="user-create"),  
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name="user-update"), 
    path('user/details/<int:pk>/', UserDetailView.as_view(), name="user-details"), 
    path('user/delete/<int:pk>/',UserDeleteView.as_view(), name="user-delete"), 
    
]
