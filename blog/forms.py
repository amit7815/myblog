from django import forms
from captcha.fields import CaptchaField

class signUpForm(forms.Form):
    username=forms.CharField(label='Username', max_length=100)
    password=forms.CharField(label="password",widget=forms.PasswordInput)
    repassword=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    captcha=CaptchaField()