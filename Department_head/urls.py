from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('getdetails/',views.getdetails,name='getdetails'),
    path('delete1/<int:did>/',views.delete1,name='delete1'),
    path('edithead/<int:did>/',views.edithead,name='edithead'),
    path('update1/<int:did>/',views.update1,name='update1'),
    path('head_view/',views.head_view,name='head_view'),
    path('employee/',views.employee,name='employee'),
    path('getemployee/',views.getemployee,name='getemployee'),
    path('delete2/<int:did>/',views.delete2,name='delete2'),
    path('employeeedit/<int:did>/',views.employeeedit,name='employeeedit'),
    path('empupdate/<int:did>/',views.empupdate,name='empupdate'),
    path('employee_view/',views.employee_view,name='employee_view')
]