from django import forms
from cbv.models import fbvmodel, ucbvmodel, pcbvmodel


class fbvform(forms.ModelForm):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    phone = forms.IntegerField()

    class Meta:
        model = fbvmodel
        fields = '__all__'

    def clean(self):
        name = self.cleaned_data['name']
        if not(name[0].isupper()):
            raise forms.ValidationError(
                "plz check username first character should be uuper case")


class ucbvform(forms.ModelForm):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    phone = forms.IntegerField()

    class Meta:
        model = ucbvmodel
        fields = '__all__'

    def clean(self):
        name = self.cleaned_data['name']
        if not(name[0].isupper()):
            raise forms.ValidationError(
                "plz check username first character should be uuper case")


class pcbvform(forms.ModelForm):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    phone = forms.IntegerField()

    class Meta:
        model = pcbvmodel
        fields = '__all__'

    def clean(self):
        name = self.cleaned_data['name']
        if not(name[0].isupper()):
            raise forms.ValidationError(
                "plz check username first character should be uuper case")
