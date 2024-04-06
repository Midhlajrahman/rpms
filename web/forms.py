from django import forms
from .models import CarreerEnquiry,Contact,DemoRegister ,CourseEnquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class CourseEnquiryForm(forms.ModelForm):
    class Meta:
        model = CourseEnquiry
        fields = "__all__"

class CareerEnquiryForm(forms.ModelForm):
    class Meta:
        model = CarreerEnquiry
        fields = "__all__"
        widgets = {
            'job_role': forms.Select(attrs={'class': 'form-select'}),
            'willing_to_work': forms.Select(attrs={'class': 'form-select'}),
            'currently_employed': forms.Select(attrs={'class': 'form-select'}),
            'hear_about_us': forms.Select(attrs={'class': 'form-select'})
    
        }
       
       
       
class DemoRegisterForm(forms.ModelForm):
    class Meta:
        model = DemoRegister
        fields = "__all__"
        widgets = {
            'course': forms.Select(attrs={'class': 'form-select'}),
    
        }