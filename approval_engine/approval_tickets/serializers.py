from rest_framework import serializers
from .models import ApprovalTicket


class ApprovalTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalTicket
        fields = "__all__"
