from django import forms
from authe.models import registermodel
from django.contrib.auth.hashers import make_password


class registerform(forms.ModelForm):
    reapssword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = registermodel
        fields = ['username',  'email', 'img', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
