from django.shortcuts import render
from myapp.models import person,Automobile
from django.http import HttpResponse
# Create your views here.
def index(request):
    print(request)
    return render(request,'register.html')

def app(request):
    user=request.GET['user']
    email=request.GET['email']
    mob=request.GET['mobile']
    person.objects.create(user=user,email=email,mobile=mob)
    return render(request,'app.html',{'user':user,'email':email,'mob':mob})

def Autoview(request):
    if request.method =='POST':
        type=request.POST['type']
        vname=request.POST.get('vname')
        cname=request.POST['cname']
        year=request.POST['year']
        price=request.POST['price']
        Automobile.objects.create(type=type,vname=vname,cname=cname,year=year,price=price)
        return HttpResponse('data is stored')
    return render(request,'automobile.html')

def AutoRead(request):
    data=Automobile.objects.all()
    return render(request,'readauto.html',{'data':data})

def Auto_One(request,pk):
    data=Automobile.objects.get(id=pk)
    return render(request,'readone.html',{'data':data})

def Auto_update(request,pk):
    data=Automobile.objects.get(id=pk)
    if request.method=='POST':
        type=request.POST['type']
        vname=request.POST.get('vname')
        cname=request.POST['cname']
        year=request.POST['year']
        price=request.POST['price']
        Automobile.objects.filter(id=pk).update(type=type,vname=vname,cname=cname,year=year,price=price)
        return HttpResponse('data is updated')
    return render(request,'readupdate.html',{'data':data})

def Auto_delete(request,pk):
    data=Automobile.objects.get(id=pk)
    if request.method=='POST':
        data=Automobile.objects.get(id=pk).delete()
        return HttpResponse('data has been deleted')
    return render(request,'delete.html',{'data':data})