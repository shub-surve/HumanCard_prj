from rest_framework import serializers
from .models import HumanCard

class HumanCardSerialized(serializers.ModelSerializer):
    class Meta:
        model = HumanCard
        fields = "__all__"
        