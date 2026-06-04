from django.http import HttpResponse
from django.shortcuts import render,redirect,get_list_or_404
from .forms import ContactForm, loginForm, regForm
from .models import Medicine, Contact

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


def login(request):
    error_message = None
    form = loginForm()

    if request.method == 'POST':
        form = loginForm(request.POST)

        if form.is_valid():
            form.save()  # optional
        else:
            error_message = "Invalid username or password."

    return render(request, 'login.html', {
        'form': form,
        'error_message': error_message
    })
def user_interface(request):
    return render(request, 'user_interface.html')
def logout(request):
    return render(request, 'logout.html')