from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
        help_text = {k: "" for k in fields}

# Hasta aca vamos bien

class UserEditForm(UserChangeForm):
    password = None
    first_name = forms.CharField(label="Nombre:" )
    last_name = forms.CharField(label="Apellido:" )
    email = forms.EmailField(label="Email", required=False)
    imagen = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "imagen"]
        
        # help_text = {k: "" for k in fields}