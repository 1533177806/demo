from django import forms


class User(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=60)
    password = forms.CharField(max_length=20)