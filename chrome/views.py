from django.shortcuts import render,redirect
from . models import Biznews,Doler,Breaking
from . form  import BiznewsForm

def index(request):
    biz=Biznews.objects.all()
    do=Doler.objects.all()
    br=Breaking.objects.all()
    context = {
        "biz":biz,
        "do":do,
        "br":br,
    }
    return render(request,"index.html",context)    
def post(request):
    form=BiznewsForm()
    context = {
        "form":form   
    }
    if request.method=="POST":
        Biznews=BiznewsForm(request.POST, request.FILES)
        if Biznews.is_valid():
            Biznews.save()
            return redirect("home")
    return render(request,"post.html",context)
