from rest_framework import serializers
from .models import DemoModel

class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model=DemoModel
        fields="__all__"

    def validate_age(self,value):
        if value<18:
            raise serializers.ValidationError("Age below 18 is not allowed!!")
        return value