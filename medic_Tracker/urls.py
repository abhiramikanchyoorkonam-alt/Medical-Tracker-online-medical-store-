from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home.html'), 
    path('home/', views.home, name='home.html'),
    path('about/', views.about, name='about.html'),
    path('contact/', views.contact, name='contact.html'),
    path('search/', views.search, name='search.html'),    
    path('reg_form/', views.reg_form, name='reg_form.html'),
    path('logout/', views.logout, name='logout.html'),
    path('login/', views.login, name='login.html'),
    path('main/',views.admin_interface,name='main.html'),
    path('main/',views.admin_interface,name='main.html'),
    path('add/',views.add_medicine,name='add_medicine'),
    path('edit/<int:id>/',views.edit_medicine,name='edit_medicine'),
    path('delete/<int:id>/',views.delete_medicine,name='delete_medicine'),
]