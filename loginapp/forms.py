from django import forms
from django.contrib.auth import login,authenticate


class LoginForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(attrs= {'placeholder':'UserName'}))
    password= forms.CharField(widget=forms.PasswordInput(attrs= {'placeholder':'Password'}))

    def clean(self, *args, **kwargs):
        username= self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('invalid username or password')
        if not user.is_active:
            raise forms.ValidationError('user is not active')
        if not user.check_password(password):
            raise forms.ValidationError('invalid password')
        return super(LoginForm,self).clean(*args, **kwargs)
