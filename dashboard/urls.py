from django.urls import path
from dashboard.views import DashboardListView, create_transaction, get_exchange_rate

urlpatterns = [
    path('', DashboardListView.as_view(), name="dashboard"), 
    path('api/exchange-rate/', get_exchange_rate, name='get_exchange_rate'),
    path('transactions/create/', create_transaction, name='create_transaction'),

]
