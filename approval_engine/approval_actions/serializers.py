from rest_framework import serializers
from .models import ApprovalAction


class ApprovalActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalAction
        fields = "__all__"
