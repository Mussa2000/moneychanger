from django.contrib import admin
from receivables.models.bank import Bank
from receivables.models.payment import Payment
from receivables.models.product import Product
from receivables.models.transaction import Transaction

# Register your models here.
admin.site.register(Bank)
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(Payment)