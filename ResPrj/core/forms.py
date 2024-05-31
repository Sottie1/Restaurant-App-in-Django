from django import forms
from .models import contact, MenuReview


class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['name', 'email', 'phone', 'subject', 'message',]

       


class MenuReviewForm(forms.ModelForm):
    

    class Meta:
        model = MenuReview
        fields = ['name', 'email', 'text']
