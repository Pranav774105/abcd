
'''
from django import forms
from .models import Student

class StudentForm(forms.Form):
    id = forms.DecimalField()
    name = forms.CharField()
    marks = forms.DecimalField()

    # Save method to create or update a Student object
    def save(self, commit=True, instance=None):
        data = self.cleaned_data
        if instance:  # If an existing instance is provided, update it
            for field, value in data.items():
                setattr(instance, field, value)
        else:  # Otherwise, create a new instance
            instance = Student(**data)
        if commit:
            instance.save()
        return instance
'''

from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta :
        model = Student
        fields = '__all__'
