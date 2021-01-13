from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import  UserCreationForm,UserChangeForm
from django.forms import ModelForm,TextInput,NumberInput,EmailInput,PasswordInput,Select,FileInput
from userprofile.models import USerprofile


class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=100,label="username",widget=forms.TextInput(attrs={'placeholder': 'write your name',}))
    email=forms.EmailField(max_length=100,label="email",widget=forms.EmailInput(attrs={'placeholder': 'enter your email',}))
    first_name=forms.CharField(max_length=100,label="first_name",widget=forms.TextInput(attrs={'placeholder':'enter your first_name'}))
    last_name=forms.CharField(max_length=100,label="last_name",widget=forms.TextInput(
        attrs={'placeholder':'enter your last_name'}
    ))

    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']
        widgets={
            'password1':forms.PasswordInput(attrs={'placeholder':'Enter New password','class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Enter re password', 'class': 'form-control'}),
        }
class UserUpdateForm(UserChangeForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name')
        widgets={
            'username':TextInput(attrs={'class':'input','placeholder':'username'}),
            'email': EmailInput(attrs={'email': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
        }


CITY = [
    ('Dhaka', 'Dhaka'),
    ('Mymensign', 'Mymensign'),
    ('Rajshahi', 'Rajshahi'),
    ('Rangpur', 'Rangpur'),
    ('Barisal', 'Barisal'),
    ('Chottogram', 'Chottogram'),
    ('Khulna', 'Khulna'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model =USerprofile
        fields = ('phonenumber', 'adderess', 'city', 'country', 'image')
        widgets = {
            'phonenumber': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'adderess': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }