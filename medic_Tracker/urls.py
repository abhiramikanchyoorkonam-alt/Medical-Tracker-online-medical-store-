from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home.html'), 
    path('home/', views.home, name='home.html'),
    path('about/', views.about, name='about.html'),
    path('contact/', views.contact, name='contact.html'),
    path('search_medicines/', views.search_medicines, name='search_medicines.html'),    
    path('reg_form/', views.reg_form, name='reg_form.html'),
    path('login_form/', views.login_form, name='login_form.html'),
]