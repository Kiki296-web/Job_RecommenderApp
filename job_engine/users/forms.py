from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomRegisterForm(UserCreationForm):
    skills = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 2, "placeholder": "Enter your skills"})
    )
    preferred_job = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Preferred job"})
    )
    preferred_location = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Preferred location"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "skills", "preferred_job", "preferred_location")
