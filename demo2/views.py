from django.views import View
from django.shortcuts import HttpResponse,render


class Greeting(View):
    msg="hello all!!!!"
    def get(self,request):
        return render(request,"home.html")

class DemoView(View):
    def get(self,req):
        return HttpResponse("demo live")