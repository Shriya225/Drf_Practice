from rest_framework import serializers
from .models import DemoModel,Articles

class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model=DemoModel
        fields="__all__"

    def validate_age(self,value):
        if value<18:
            raise serializers.ValidationError("Age below 18 is not allowed!!")
        return value
    
class ArticleSerializer(serializers.ModelSerializer):
    demo=DemoSerializer()
    country=serializers.SerializerMethodField()
    def get_country(self,obj):
        return {"country":"india","place":obj.demo.place}
    class Meta:
        model=Articles
        fields="__all__"
        # depth=1
    