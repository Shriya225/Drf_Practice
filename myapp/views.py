from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DemoModel,Articles,Plant
from .serializers import DemoSerializer,ArticleSerializer,PlantSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import status


@api_view(["GET","POST"])
def index(request):
    if request.method=="POST":
        data={"name":"shriya",
            "place":"vijayawada",
            "technical skills":"c,Python,java,Django,Drf"}
        return Response(data)
    elif request.method=="GET":
        return Response({"response":"iam a get method response"})
    
@api_view(["GET","POST","PUT","PATCH","DELETE"])
def tasklist(request):
    if request.method=="GET":
        tasks=DemoModel.objects.all()
        serializer=DemoSerializer(tasks,many=True)
        return Response(serializer.data)
    
    elif request.method=="POST":
        serializer=DemoSerializer(data=request.data)
        if serializer.is_valid():
            demo_insatnce=serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method=="PUT":
        serializer=DemoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method=="PATCH":
        obj=DemoModel.objects.get(id=request.data["id"])
        serializer=DemoSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        obj=DemoModel.objects.get(id=request.data["id"])
        obj.delete()
        return Response({"msg":f"succesfully deleted {request.data["id"]} "})
    

@api_view(["GET","POST"])
def articleList(request):
    if request.method=="GET":
        x=Articles.objects.all()
        serializer=ArticleSerializer(x,many=True)
        return Response(serializer.data)
    

class PlantAPI(ViewSet):
    #get req to list all plants
    def list(self,request):
        plants=Plant.objects.all()
        serializer=PlantSerializer(plants,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        plant=Plant.objects.filter(pk=pk).first()
        if not plant:
            return Response({"msg":"not found"})
        serializer=PlantSerializer(plant)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def destroy(self,request,pk=None):
        plant=Plant.objects.filter(pk=pk)
        if not plant:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




