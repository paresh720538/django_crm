# to crete the login  and register auth we have to create this file and import the auth and user manually


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput,TextInput
from .models import Record

# register / create a user 

class CreateUserForm(UserCreationForm):
    
    class meta:
        
        model = User
        fields = ["username",'password1','password2']

#Login a user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

#CREATE A RECORD
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','address','city','province','country']
        
# UPDATE A RECORD     
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','address','city','province','country']