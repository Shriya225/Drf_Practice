from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DemoModel
from .serializers import DemoSerializer

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