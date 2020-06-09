from django.shortcuts import render

# Create your views here.

def boot(request):
    return render(request,'boot.html')

def boot1(request):
    return render(request,'boot1.html')

def extend(request):
    return render(request,'extend.html')
