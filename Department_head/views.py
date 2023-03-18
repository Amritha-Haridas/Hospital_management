from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from adminapp.models import *

# Create your views here.
def index(request):
    data = Departmentsdb.objects.all()
    return render(request,'index.html',{'data':data})
    

def getdetails(request):
    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        images = request.FILES['images']
        age = request.POST.get('age')
        des = request.POST.get('des')
        data1 = Headdb(name=name,images=images,age=age,number=number)
        data1.save()
        return redirect('index') 

def delete1(request,did):
    Departmentsdb.objects.filter(id=did).delete()
    return redirect('head_view')

def edithead(request,did):
    data = Departmentsdb.objects.filter(id=did)
    return render(request,'edithead.html',{'data':data})   

def update1(request,did):
    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        age = request.POST.get('age')
        des = request.POST.get('des')
        try:
            img_c = request.FILES['images']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file =Headdb .objects.get(id=did).images
        Headdb.objects.filter(id=did).update(name=name,images=file,age=age,number=number)
        return redirect('head_view') 

def head_view(request):
    data = Headdb.objects.all()
    return render(request,'head_view.html',{'data':data})

def employee(request):
    datas = Headdb.objects.all()
    data = Departmentsdb.objects.all()
    return render(request,'employee.html',{'data':data,'datas':datas})
    

def getemployee(request):
    if request.method=="POST":
        name = request.POST.get('ename')
        number = request.POST.get('enumber')
        images = request.FILES['eimages']
        age = request.POST.get('eage')
        des = request.POST.get('desc')
        report = request.POST.get('report')
        data2 = Headdb(ename=ename,eimages=eimages,eage=eage,enumber=enumber,report=report)
        data2.save()
        return redirect('employee') 

def delete2(request,did):
    Employeedb.objects.filter(id=did).delete()
    return redirect('head_view')

def employeeedit(request,did):
    data = Employeedb.objects.filter(id=did)
    return render(request,'employeeedit.html',{'data':data})   

def empupdate(request,did):
    if request.method=="POST":
        ename = request.POST.get('ename')
        enumber = request.POST.get('enumber')
        eage = request.POST.get('eage')
        des = request.POST.get('des')
        report = request.POST.get('report')
        try:
            img_c = request.FILES['eimages']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file =Headdb .objects.get(id=did).eimages
        Headdb.objects.filter(id=did).update(ename=ename,eimages=eimages,eage=eage,enumber=enumber,report=report)
        return redirect('employee_view') 

def employee_view(request):
    data = Employeedb.objects.all()
    return render(request,'employee_view.html',{'data':data})


