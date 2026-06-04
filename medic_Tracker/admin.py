from django.contrib import admin
from .models import Medicine
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