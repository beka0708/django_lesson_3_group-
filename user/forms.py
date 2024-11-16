from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=True)
    phone_number = forms.IntegerField(required=True)

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "citi",
            "image",
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
