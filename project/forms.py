from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

# from users.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)    
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password1']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')

        return username