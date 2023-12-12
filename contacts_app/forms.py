# contacts_app/forms.py

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'  # Include all fields from your Contact model, or specify fields explicitly
