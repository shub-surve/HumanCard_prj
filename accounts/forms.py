from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import HumanCard , Contact

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username' , 'email', 'password']


class HumanCardForm(forms.ModelForm):
    class Meta:
        model = HumanCard
        fields = ['first_name', 'last_name', 'age', 'blood_group', 'address', 'phone_number', 'email', 'profile_pic']



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

from django import forms
from .models import Contact  # Adjust the import based on your project structure

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'query']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'required': 'required'
            }),
            'query': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type your query here...',
                'rows': 5,
                'required': 'required'
            }),
        }
        labels = {
            'email': 'Your Email',
            'query': 'Your Query',
        }
        help_texts = {
            'email': 'We will never share your email with anyone else.',
            'query': 'Please provide as much detail as possible.',
        }
        error_messages = {
            'email': {
                'required': 'Email is required.',
                'invalid': 'Enter a valid email address.',
            },
            'query': {
                'required': 'Query cannot be empty.',
            },
        }
