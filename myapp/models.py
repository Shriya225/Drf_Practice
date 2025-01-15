from django.db import models

# Create your models here.
class DemoModel(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return self.name

class Articles(models.Model):
    demo=models.ForeignKey(DemoModel,on_delete=models.CASCADE,related_name="DemoModel")
    title=models.CharField(max_length=30)
    pages=models.IntegerField()

    def __str__(self):
        return self.title
    
class Plant(models.Model):
    name=models.CharField(max_length=30)
    color=models.CharField(max_length=10)
    age=models.IntegerField()


    
