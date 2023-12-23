from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from logger import colored_logger as logger


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'username')

    def __init__(self, *args, **kwargs):
        logger.debug("🚀 ~ file: forms.py ~ CustomUserCreationForm ~ __init__ ~ args:", args)
        logger.debug("🚀 ~ file: forms.py ~ CustomUserCreationForm ~ __init__ ~ kwargs:", kwargs)
        
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'First Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Last Name'})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['username'].required = False
        
        for fieldname in ['first_name', 'last_name', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean(self):
        logger.debug("🚀 ~ file: forms.py ~ CustomUserCreationForm ~ clean ~ self.cleaned_data:", self.cleaned_data)
        return self.cleaned_data
    
    def clean_email(self):
        logger.debug("🚀 ~ file: forms.py ~ CustomUserCreationForm ~ clean_email ~ self.cleaned_data:", self.cleaned_data)
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email
    
    def clean_password2(self):
        logger.debug("🚀 ~ file: forms.py ~ CustomUserCreationForm ~ clean_password2 ~ self.cleaned_data:", self.cleaned_data)
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        
        return password2
    
    def clean_username(self):
        logger.debug("🚀 ~ file: forms.py ~ CustomUserCreationForm ~ clean_username ~ self.cleaned_data:", self.cleaned_data)
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        username = f"{first_name.lower()}.{last_name.lower()}"

        User = get_user_model()
        if User.objects.filter(username=username).exists():
            counter = 1
            while User.objects.filter(username=f"{username}.{counter}").exists():
                counter += 1
            username = f"{username}.{counter}"
        return username
    
    def save(self, commit=True):
        logger.debug("🚀 ~ file: forms.py ~ CustomUserCreationForm ~ save ~ self.cleaned_data:", self.cleaned_data)
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user
