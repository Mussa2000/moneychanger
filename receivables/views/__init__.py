from receivables.views.transaction import (
    TransactionListView,
    TransactionCreateView,
    TransactionUpdateView,
    TransactionDetailsView,
    TransactionDeleteView,
)

from receivables.views.bank import (
    BankListView,
    BankCreateView,
    BankUpdateView,
    BankDetailsView,
    BankDeleteView,
    ExportBankTransactionsToExcelView,
    
)
from receivables.views.product import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDetailsView,
    ProductDeleteView,
    
)
from receivables.views.payment import (
    PaymentListView,
    PaymentCreateView,
    PaymentUpdateView,
    PaymentDetailsView,
    PaymentDeleteView,

)

from receivables.views.province import (
    ProvinceListView,
    ProvinceCreateView,
    ProvinceUpdateView,
    ProvinceDetailsView,
    ProvinceDeleteView,
)

