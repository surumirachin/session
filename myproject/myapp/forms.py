from django import forms

CHOICES = [('Male','Male'),('Female','Female'),('Others','Others')]

class EmailLogin(forms.Form):
    email = forms.EmailField(max_length=100,required=True)
    full_name = forms.CharField(max_length=50, required=True)
    age = forms.IntegerField(required=True)
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))

