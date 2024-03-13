from django.urls import path
from dashboard.views import DashboardListView

urlpatterns = [
    path('', DashboardListView.as_view(), name="dashboard"),   
]
