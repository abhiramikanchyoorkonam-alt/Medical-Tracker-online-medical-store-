from django.http import HttpResponse
from django.shortcuts import render,redirect,get_list_or_404
from .forms import ContactForm, regForm
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


def search_medicines(request):
    query = request.GET.get('q')
    if query:
        medicines = Medicine.objects.filter(name__icontains=query)
    else:
        medicines = Medicine.objects.all()
    return render(request, 'search_medicines.html', {'medicines': medicines})   
