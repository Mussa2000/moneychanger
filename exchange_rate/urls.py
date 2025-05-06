from django.urls import path
from . import views

urlpatterns = [
    # Currency URLs
    path('currencies/', views.CurrencyListView.as_view(), name='currency-index'),
    path('currencies/create/', views.CurrencyCreateView.as_view(), name='currency-create'),
    path('currencies/<int:pk>/edit/', views.CurrencyUpdateView.as_view(), name='currency-edit'),
    path('currencies/<int:pk>/delete/', views.CurrencyDeleteView.as_view(), name='currency-delete'),

    # Exchange Source URLs
    path('sources/', views.ExchangeSourceListView.as_view(), name='source-index'),
    path('sources/create/', views.ExchangeSourceCreateView.as_view(), name='source-create'),
    path('sources/<int:pk>/edit/', views.ExchangeSourceUpdateView.as_view(), name='source-edit'),
    path('sources/<int:pk>/delete/', views.ExchangeSourceDeleteView.as_view(), name='source-delete'),

    # Exchange Rate URLs
    path('rates/', views.ExchangeRateListView.as_view(), name='rate-index'),
    path('rates/create/', views.ExchangeRateCreateView.as_view(), name='rate-create'),
    path('rates/<int:pk>/edit/', views.ExchangeRateUpdateView.as_view(), name='rate-edit'),
    path('rates/<int:pk>/delete/', views.ExchangeRateDeleteView.as_view(), name='rate-delete'),
    
    # User Exchange Rate URLs
    path('user/rates/', views.UserExchangeRateListView.as_view(), name='user-rate-index'),
    path('user/rates/create/', views.UserExchangeRateCreateView.as_view(), name='user-rate-create'),
    path('user/rates/<int:pk>/edit/', views.UserExchangeRateUpdateView.as_view(), name='user-rate-edit'),
    path('user/rates/<int:pk>/delete/', views.UserExchangeRateDeleteView.as_view(), name='user-rate-delete'),
    
    # Transaction URLs
    path('transactions/list/', views.TransactionListView.as_view(), name='transaction-index'),
    path('transactions/proposals/', views.ExchangeProposalListView.as_view(), name='proposal-index'),
    path('transactions/proposals/<int:pk>/edit/', views.ExchangeProposalUpdateView.as_view(), name='proposal-edit'),
]
