from rest_framework import serializers
from .models import Approver


class ApproverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approver
        fields = "__all__"
