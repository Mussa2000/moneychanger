from rest_framework import serializers
from .models import ApprovalGroup


class ApprovalGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalGroup
        fields = "__all__"
