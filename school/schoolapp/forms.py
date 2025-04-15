from django import forms
from schoolapp.models import School

class SchoolForm(forms.ModelForm):
    location_choices = [('ernakulam','EKM'),('Trivandrum','TVM'),('Kannur','CNN')]
    location = forms.ChoiceField(choices=location_choices, widget=forms.Select, required=True)
    class Meta:
        model = School
        fields = ['name','principal','location']