from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import Medicine
class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(
        attrs = {
        'class':'form-control',
        'placeholder':'Username'
        }
    ))
    first_name = forms.CharField(required=True,widget=forms.TextInput(
        attrs = {
        'class':'form-control',
        'placeholder':'Your First name'
        }
    ))
    last_name = forms.CharField(required=True,widget=forms.TextInput(
        attrs = {
        'class':'form-control',
        'placeholder':'Your Last name'
        }
    ))
    email = forms.CharField(required=True,widget=forms.EmailInput(
        attrs = {
        'class':'form-control',
        'placeholder':'Your Email Id'
        }
    ))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(
        attrs = {
        'class':'form-control',
        'placeholder':'Password'
        }
    ))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(
        attrs = {
        'class':'form-control',
        'placeholder':'Confirm Password'
        }
    ))


    class Meta:
        model = User
        fields = ('username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
            )

    def save(self,commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class add(forms.ModelForm):
    class Meta:
        model = Medicine
        fields=(
        'name',
        'price',
        'company',
        'des',
        )
