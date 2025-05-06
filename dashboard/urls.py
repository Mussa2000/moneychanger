from django.urls import path
from dashboard.views import DashboardListView, accept_proposal_view, create_exchange_proposal, create_transaction, get_exchange_rate, get_seller_rates, reject_proposal_view

urlpatterns = [
    path('', DashboardListView.as_view(), name="dashboard"), 
    path('api/exchange-rate/', get_exchange_rate, name='get_exchange_rate'),
    path('api/seller-rates/', get_seller_rates, name='get_seller_rates'),
    path('transactions/create/', create_transaction, name='create_transaction'),
    path('create-exchange-proposal/', create_exchange_proposal, name='create_exchange_proposal'),
    path('proposals/<int:pk>/accept/', accept_proposal_view, name='accept_proposal'),
    path('proposals/<int:pk>/reject/', reject_proposal_view, name='reject_proposal'),

]
