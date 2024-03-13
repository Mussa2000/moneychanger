from rest_framework import serializers
from .models import ApprovalGroupLevel


class ApprovalGroupLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalGroupLevel
        fields = "__all__"
