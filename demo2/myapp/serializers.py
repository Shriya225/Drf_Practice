from rest_framework.serializers import ModelSerializer
from .models import DemoModel

class DemoSerializer(ModelSerializer):
    class Meta:
        model=DemoModel
        fields="__all__"