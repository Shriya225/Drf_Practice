from django.urls import path,include
from myapp.views import index,tasklist

urlpatterns = [
    path("index/",index,name="index"),
    path("tasklist/",tasklist),
   ]