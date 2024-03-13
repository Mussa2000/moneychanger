from rest_framework import serializers
from .models import ApprovalGroupMark


class ApprovalGroupMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalGroupMark
        fields = "__all__"
