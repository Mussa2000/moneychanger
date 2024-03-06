from rest_framework import serializers
from .models import ApprovalMark


class ApprovalMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalMark
        fields = "__all__"
