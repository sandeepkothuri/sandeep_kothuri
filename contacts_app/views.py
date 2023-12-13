from django.shortcuts import render
from .models import Contact

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts_pages/list_contacts.html', {'contacts': contacts})

from django.shortcuts import render, redirect
from .forms import ContactForm  # You need to create this form in forms.py

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_contacts')
    else:
        form = ContactForm()

    return render(request, 'contacts_pages/create_contacts.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('list_contacts')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contacts_pages/update_contacts.html', {'form': form})

from django.shortcuts import redirect, get_object_or_404
from .models import Contact

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('list_contacts')
    return render(request, 'contacts_pages/delete_contacts.html', {'contact': contact})

from django.shortcuts import render, get_object_or_404

def view_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts_pages/view_contact.html', {'contact': contact})









    

