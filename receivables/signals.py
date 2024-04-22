from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Payment, Transaction

@receiver(post_save, sender=Payment)
def update_transaction_amount_paid(sender, instance, created, **kwargs):
    if created:
        # Get the corresponding transaction for the payment
        transaction = instance.transaction
        if transaction:
            transaction.amount_paid += instance.amount
            transaction.save()
        
@receiver(post_delete, sender=Payment)
def update_transaction_amount_paid_on_delete(sender, instance, **kwargs):
    # Get the corresponding transaction for the deleted payment
    transaction = instance.transaction
    if transaction:
        transaction.amount_paid -= instance.amount
        transaction.save()
        
@receiver(post_save, sender=Payment)
def update_transaction_status(sender, instance, **kwargs):
    # Get the corresponding transaction for the payment
    transaction = instance.transaction
    if transaction:
        total_amount = transaction.total()
        if transaction.amount_paid >= total_amount:  # Check if amount paid is greater than or equal to the total amount
            transaction.status = 'Paid'  # Update transaction status to 'Paid'
        else:
            transaction.status = 'Pending'  # Update transaction status to 'Pending' if amount paid is less than total amount
        
        transaction.save()
