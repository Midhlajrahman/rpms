# web/forms.py
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact
from .models import ServiceEnquiry
from django.forms import widgets


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your Name*"}),
            "phone": widgets.TextInput(attrs={"class": "required form-control", 'type': 'number',"placeholder": "Your Phone*"}),
            "email": widgets.EmailInput(attrs={"class": "required form-control","placeholder": "Your Email*",}),
            "subject": widgets.TextInput(attrs={"class": "required form-control","placeholder": "Subject",}),
            "message": widgets.Textarea(attrs={"class": "required form-control","placeholder": "Enter Your Message*",}),
        }

class ServiceEnquiryForm(forms.ModelForm):
    class Meta:
        exclude = ("service",)
        model = ServiceEnquiry
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control input required", "placeholder": "Name"}),
            "mobile": widgets.TextInput(
                attrs={"class": "required form-control input", 'type': 'number', "placeholder": "Mobile"}
            ),
            "email": widgets.EmailInput(attrs={"class": "required form-control input", "placeholder": "Email"}),
            "message": widgets.Textarea(attrs={"class": "required form-control input", "placeholder": "Message",'rows':4, 'cols':15}),
        }