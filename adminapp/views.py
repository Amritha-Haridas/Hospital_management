from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
# Create your views here.
def departments(request):
    return render(request,'departments.html')

def getData(request):
    if request.method=="POST":
        departmentname = request.POST.get('departmentname')
        profileimage = request.FILES['profileimage']
        yearfounded = request.POST.get('yearfounded')
        description = request.POST.get('description')
        data = Departmentsdb(departmentname=departmentname,profileimage=profileimage,yearfounded=yearfounded,description = description)
        data.save()
        return redirect('departments') 

def department_view(request):
    data = Departmentsdb.objects.all()
    print(data)
    return render(request,'department_view.html',{'data':data})


def delete(request,did):
    Departmentsdb.objects.filter(id=did).delete()
    return redirect('department_view')

def edit(request,did):
    data = Departmentsdb.objects.filter(id=did)
    return render(request,'edit.html',{'data':data})   

def update(request,did):
    if request.method=="POST":
        departmentname = request.POST.get('departmentname')
        yearfounded = request.POST.get('yearfounded')
        description = request.POST.get('description')
        try:
            img_c = request.FILES['profileimage']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file =Departmentsdb .objects.get(id=did).profileimage
        Departmentsdb.objects.filter(id=did).update(departmentname=departmentname,profileimage=file,yearfounded=yearfounded,description = description)
        return redirect('department_view') 


def login(request):
    return render(request,'login.html')


def getvalue(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        data=Logindb(username=username, password=password)
        request.session['usernamead'] = username
        request.session['passwordad'] = password
        return redirect('departments')
    else:
        return render(request, 'login.html')

def logout(request):
    del request.session['usernamead']
    del request.session['passwordad']
    return redirect('login')