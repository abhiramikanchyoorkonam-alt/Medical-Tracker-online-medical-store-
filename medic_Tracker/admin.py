from django.contrib import admin
from .models import Medicine, login, logout, registration, user_interface
from .models import Contact

# Register your models here.
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage', 'price', 'start_date', 'end_date')
    search_fields = ('name',)
admin.site.register(Medicine, MedicineAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email')
admin.site.register(Contact, ContactAdmin)

class registrationAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'address','age','gender','blood_group','state','password','created_at')
    search_fields = ('username', 'email')
admin.site.register(registration, registrationAdmin)

class loginAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    search_fields = ('username',)
admin.site.register(login, loginAdmin)

class user_interfaceAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    search_fields = ('username',)   
admin.site.register(user_interface, user_interfaceAdmin)

class logoutAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    search_fields = ('username',)
admin.site.register(logout, logoutAdmin)

