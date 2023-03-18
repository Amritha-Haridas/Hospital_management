from django.urls import path
from . import views

urlpatterns = [
    path('departments/',views.departments,name='departments'),
    path('getData',views.getData,name='getData'),
    path('department_view/',views.department_view,name='department_view'),
    path('delete/<int:did>/',views.delete,name='delete'),
    path('edit/<int:did>/',views.edit,name='edit'),
    path('update/<int:did>/',views.update,name='update'),
    path('login/',views.login,name='login'),
    path('getvalue/',views.getvalue,name='getvalue'),
    path('logout/',views.logout,name='logout')
]
