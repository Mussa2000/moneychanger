from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal

from exchange_rate.models import ExchangeAgreement, Transaction

@receiver(post_save, sender=ExchangeAgreement)
def handle_agreement_status(sender, instance, created, **kwargs):
    if instance.status == 'Accepted':
        # Check if transaction already exists
        existing_txn = Transaction.objects.filter(agreement=instance).first()
        if existing_txn:
            return  # Don't duplicate

        proposal = instance.proposal
        proposal.status = 'Accepted'
        proposal.save()
        
        seller_rate = proposal.seller_rate

        # Create transaction
        Transaction.objects.create(
            transaction_type='Buy',  # Adjust if you plan to allow Sell from proposal later
            base_currency=seller_rate.base_currency,
            target_currency=seller_rate.target_currency,
            amount=proposal.amount,
            rate=proposal,
            agreement=instance,
            received_amount=(proposal.amount * proposal.proposed_rate)
        )
        
        exchange_agreement = ExchangeAgreement.objects.filter(proposal=proposal).first()
        if exchange_agreement:
            exchange_agreement.status = 'Accepted'
            exchange_agreement.save()

    elif instance.status == 'Cancelled':
        # Optional: handle cleanup or notification
        pass

    elif instance.status == 'Completed':
        # Optional: update wallet balances or logs
        pass
