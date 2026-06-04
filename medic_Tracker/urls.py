from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home.html'), 
    path('home/', views.home, name='home.html'),
    path('about/', views.about, name='about.html'),
    path('contact/', views.contact, name='contact.html'),
    path('search/', views.search, name='search.html'),    
    path('reg_form/', views.reg_form, name='reg_form.html'),
    path('login/', views.login, name='login.html'),
    path('logout/', views.logout, name='logout.html'),
    path('login/<str:username>/<str:password>/', views.login, name='login.html'),
    path('user_interface/', views.user_interface, name='user_interface.html'),
]