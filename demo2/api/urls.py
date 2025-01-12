from django.urls import path,include
from myapp.views import index,tasklist,articleList

urlpatterns = [
    path("index/",index,name="index"),
    path("tasklist/",tasklist),
    path("ArticleList/",articleList),
   ]