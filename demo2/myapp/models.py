from django.db import models

# Create your models here.
class DemoModel(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=50)
    age=models.IntegerField()

class Articles(models.Model):
    demo=models.ForeignKey(DemoModel,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    pages=models.IntegerField()



    
