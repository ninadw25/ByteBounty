from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def home(request):
    #return HttpResponse("Hello This is ByteBounty website")
    
def mainpage(request):
        return render(request,'mainpage.html')

