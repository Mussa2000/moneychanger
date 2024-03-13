from rest_framework import serializers
from .models import ApprovalGroupAction


class ApprovalGroupActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalGroupAction
        fields = "__all__"
