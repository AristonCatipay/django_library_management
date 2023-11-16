from django import forms
from .models import Thesis, Author, Author_List

INPUT_CLASSES = 'rounded-md bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
FOR_IMAGE = 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'

class ThesisForm(forms.ModelForm):
    class Meta: 
        model = Thesis
        fields = ['title', 'date_published', 'course', 'image', 'file']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'date_published' : forms.SelectDateWidget(years=range(1500, 2999), attrs={
                'class': INPUT_CLASSES,
            }),
            'course': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': FOR_IMAGE,
            }),
            'file': forms.FileInput(attrs={
                'class': FOR_IMAGE,
            }),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'image', 'course']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'last_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'course': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': FOR_IMAGE
            }),
        }

class AuthorListForm(forms.ModelForm):
    class Meta:
        model = Author_List
        fields = ['author']
        widgets = {
            'author': forms.Select(attrs={
                'class': INPUT_CLASSES,
            })
        }