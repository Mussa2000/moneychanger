from rest_framework import serializers
from .models import ApprovalLevel


class ApprovalLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalLevel
        fields = "__all__"
