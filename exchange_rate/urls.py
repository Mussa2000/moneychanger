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
]
