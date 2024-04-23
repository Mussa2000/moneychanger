from django.db.models import Count, Sum, F, ExpressionWrapper, DecimalField,  Case, When

from accounts.models.user import CustomUser

class ProvinceStats:
    @classmethod
    def get_stats(cls):
        # Query to get province-wise statistics
        province_stats = (
            CustomUser.objects.filter(is_farmer=True)
            .values('province__name')
            .annotate(
                num_farmers=Count('id'),
                total_amount=Sum(
                    ExpressionWrapper(F('transaction__quantity') * F('transaction__product__unit_cost'),
                    output_field=DecimalField(decimal_places=2))
                ),
                partially_paid=Sum(
                    Case(
                        When(transaction__status='pending', then=F('transaction__amount_paid')),
                        default=0,
                        output_field=DecimalField(decimal_places=2),
                    )
                ),
            )
        )
        return province_stats
