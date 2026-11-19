from django import forms

class Student_form_data(forms.Form):
    reg_no = forms.CharField(max_length=20)
    name = forms.CharField(max_length=100)
    marks = forms.FloatField()
    email = forms.EmailField()
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )