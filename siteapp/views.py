from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"siteapp/home.html")
def learn(request):
    return render(request,"siteapp/learn.html")
def login(request):
    return render(request,"siteapp/login.html")
def practice(request):
    return render(request,"siteapp/practice.html")
def jobs(request):
    return render(request,"siteapp/jobs.html")
def homee(request):
    return render(request,"siteapp/home.html")