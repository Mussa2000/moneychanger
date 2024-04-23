from django.urls import path
from receivables.views import (
    TransactionListView,
    TransactionCreateView,
    TransactionUpdateView,
    TransactionDetailsView,
    TransactionDeleteView,
    
    BankListView,
    BankCreateView,
    BankUpdateView,
    BankDetailsView,
    BankDeleteView,
    ExportBankTransactionsToExcelView,
    
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDetailsView,
    ProductDeleteView,
    
    PaymentListView,
    PaymentCreateView,
    PaymentUpdateView,
    PaymentDetailsView,
    PaymentDeleteView,
    
    ProvinceListView,
    ProvinceCreateView,
    ProvinceUpdateView,
    ProvinceDetailsView,
    ProvinceDeleteView,
)

urlpatterns = [
    path('bank/index/', BankListView.as_view(), name="bank-index"), 
    path('bank/create/', BankCreateView.as_view(), name="bank-create"),  
    path('bank/update/<int:pk>/', BankUpdateView.as_view(), name="bank-update"), 
    path('bank/details/<int:pk>/', BankDetailsView.as_view(), name="bank-details"), 
    path('bank/delete/<int:pk>/', BankDeleteView.as_view(), name="bank-delete"), 
    path('bank/export/payments/<int:pk>/', ExportBankTransactionsToExcelView.as_view(), name="export-bank-payments"), 
    
    path('product/index/', ProductListView.as_view(), name="product-index"), 
    path('product/create/', ProductCreateView.as_view(), name="product-create"),  
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name="product-update"), 
    path('product/details/<int:pk>/', ProductDetailsView.as_view(), name="product-details"), 
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name="product-delete"), 
    
    path('transaction/index/',TransactionListView.as_view(), name="transaction-index"), 
    path('transaction/create/', TransactionCreateView.as_view(), name="create-transaction"),  
    path('transaction/update/<int:pk>/', TransactionUpdateView.as_view(), name="transaction-update"), 
    path('transaction/details/<int:pk>/', TransactionDetailsView.as_view(), name="transaction-details"), 
    path('transaction/delete/<int:pk>/', TransactionDeleteView.as_view(), name="transaction-delete"), 
    
    path('payment/index/',PaymentListView.as_view(), name="payment-index"), 
    path('payment/create/<int:pk>/', PaymentCreateView.as_view(), name="create-payment"),  
    path('payment/update/<int:pk>/', PaymentUpdateView.as_view(), name="payment-update"), 
    path('payment/details/<int:pk>/', PaymentDetailsView.as_view(), name="payment-details"), 
    path('payment/delete/<int:pk>/', PaymentDeleteView.as_view(), name="payment-delete"), 
    
    path('province/index/', ProvinceListView.as_view(), name="province-index"), 
    path('province/create/', ProvinceCreateView.as_view(), name="create-province"),  
    path('province/update/<int:pk>/', ProvinceUpdateView.as_view(), name="province-update"), 
    path('province/details/<int:pk>/', ProvinceDetailsView.as_view(), name="province-details"), 
    path('province/delete/<int:pk>/', ProvinceDeleteView.as_view(), name="province-delete"), 
    
    
]
