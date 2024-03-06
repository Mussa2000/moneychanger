from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.db.models import Q
from approval_engine.approval_group_levels.models import ApprovalGroupLevel, ApprovalGroupLevelProxy

def update_indices_for_records(records):
    for i, record in enumerate(records):
        record.index = i + 1
        record.save()

@receiver(pre_delete, sender=ApprovalGroupLevel)
def update_indices_on_delete(sender, instance, **kwargs):
    # Get the records with higher indices
    higher_indices = ApprovalGroupLevel.objects.filter(
        Q(index__gt=instance.index) & Q(approval_ticket=instance.approval_ticket)
    )

    # Update the indices of the remaining records
    for record in higher_indices:
        record.index -= 1
        record.save()

    # Check if the first record has index 1
    first_record = (
        ApprovalGroupLevel.objects.filter(
            Q(index__gt=instance.index) & Q(approval_ticket=instance.approval_ticket)
        )
        .order_by("index")
        .first()
    )

    if first_record and first_record.index != 1:
        # If not, update the indices to start from 1
        records_to_update = (
            ApprovalGroupLevel.objects.filter(
                Q(index__gt=instance.index) & Q(approval_ticket=instance.approval_ticket)
            )
            .order_by("index")
        )
        update_indices_for_records(records_to_update)


@receiver(pre_delete, sender=ApprovalGroupLevelProxy)
def update_indices_on_delete(sender, instance, **kwargs):
    # Get the records with higher indices
    higher_indices = ApprovalGroupLevelProxy.objects.filter(
        Q(index__gt=instance.index) & Q(approval_ticket=instance.approval_ticket)
    )

    # Update the indices of the remaining records
    for record in higher_indices:
        record.index -= 1
        record.save()

    # Check if the first record has index 1
    first_record = (
        ApprovalGroupLevelProxy.objects.filter(
            Q(index__gt=instance.index) & Q(approval_ticket=instance.approval_ticket)
        )
        .order_by("index")
        .first()
    )

    if first_record and first_record.index != 1:
        # If not, update the indices to start from 1
        records_to_update = (
            ApprovalGroupLevelProxy.objects.filter(
                Q(index__gt=instance.index) & Q(approval_ticket=instance.approval_ticket)
            )
            .order_by("index")
        )
        update_indices_for_records(records_to_update)