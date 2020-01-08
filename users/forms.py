from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=70, min_length=7)

    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput()
    )
    
    confirm_password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput()
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise forms.ValidationError('Email already exists')

        return email


    def clean(self):
        data = super().clean()

        if data['password'] != data['confirm_password']:
            raise forms.ValidationError('There is not match between the passwords')

        return data


    def save(self):
        data = self.cleaned_data
        import pdb; pdb.set_trace()

        user = User.objects.create_user(
            username=data['username'], 
            email=data['email'], 
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )

        Profile.objects.create(user=user)


class FormUpdateProfile(forms.Form):

    first_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First name'})
    )

    last_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last name'})
    )

    picture = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))

    email = forms.EmailField(max_length=70, min_length=7, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email address'})
    )


    def clean_email(self):
        email = self.cleaned_data['email']
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email already in use')
        return email


    def save(self, user):
        data = self.cleaned_data

        user = User.objects.get(pk=user.pk)
        user.first_name = data['first_name']
        user.last_name = data['last_name']

        profile = Profile.objects.get(user=user)
        profile.picture = data['picture']

        user.save()
        profile.save()
        



