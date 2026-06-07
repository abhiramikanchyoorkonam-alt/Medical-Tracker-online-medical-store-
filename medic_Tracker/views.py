from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .forms import ContactForm, LoginForm, regForm,MedicineForm
from django.contrib.auth import authenticate,login
from .models import Medicine, Contact,registration

def about(request):
    return render(request, 'about.html')
def contact(request):
    success_message = None

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            success_message = "Thank you! Your message has been sent."
            form = ContactForm()

    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'success_message': success_message
    })
def home(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})


def reg_form(request):
    success_message = None

    if request.method == 'POST':
        form = regForm(request.POST)

        if form.is_valid():
            form.save()
            success_message = "Registration successful!"
            form = regForm()

    else:
        form = regForm()

    return render(request, 'reg_form.html', {'form': form, 'success_message': success_message })



def search(request):
    query = request.GET.get('q', '')

    medicines = Medicine.objects.all()

    if query:
        medicines = Medicine.objects.filter(name__icontains=query)
    else:
        medicines=Medicine.objects.filter(name__icontains=query)

    return render(request, 'search.html', {
        'medicines': medicines,
        'query': query
    })
from .models import registration
from .forms import LoginForm

def login(request):

    error_message = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # Admin Login
        if username == "admin" and password == "password":
            return redirect('main.html')
    return render(request,'login.html',{'error_message': error_message})

def logout(request):
    return render(request, 'home.html')

def admin_interface(request):
    medicines = Medicine.objects.all()
    contacts = Contact.objects.all()
    registrations = registration.objects.all()

    print("REGISTRATIONS:", registrations)
    print("COUNT:", registrations.count())

    return render(request, 'main.html', {
        'medicines': medicines,
        'contacts': contacts,
        'registrations': registrations,
    })



def add_medicine(request):
    form = MedicineForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('main.html')

    return render(request,'add.html',{'form':form})

def edit_medicine(request,id):
    medicine = get_object_or_404(Medicine,id=id)

    form = MedicineForm(request.POST or None,instance=Medicine)

    if form.is_valid():
        form.save()
        return redirect('main.html')

    return render(request,'edit.html',{'form':form})

def delete_medicine(request, id):
    medicine = get_object_or_404(Medicine, id=id)

    if request.method == "POST":
        medicine.delete()
        return redirect('main.html')

    return render( request,'delete.html',{'medicine': medicine})

