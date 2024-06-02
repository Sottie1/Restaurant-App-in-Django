from django import forms
from .models import contact, Review, RATINGS


class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['name', 'email', 'phone', 'subject', 'message',]

       


class MenuReviewForm(forms.ModelForm):
    

    class Meta:
        model = Review
        fields = ['name', 'email', 'text', 'rating']

        widgets= {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'text': forms.Textarea(attrs={'placeholder': 'Write Review'}),
            'rating': forms.Select(choices=RATINGS),
        }
