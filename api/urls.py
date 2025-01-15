from django.urls import path,include
from myapp.views import index,tasklist,articleList,PlantAPI
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r"plant",PlantAPI,basename="plant")


urlpatterns = [
    path("index/",index,name="index"),
    path("tasklist/",tasklist),
    path("ArticleList/",articleList),
   ]+router.urls