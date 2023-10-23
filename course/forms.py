from django import forms
from .models import Course

INPUT_CLASSES = 'rounded-md bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'abbreviation']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'abbreviation': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),  
        }