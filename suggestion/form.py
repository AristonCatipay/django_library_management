from django import forms
from .models import Suggestion

INPUT_CLASSES = 'rounded-md bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
FOR_IMAGE = 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['book_title', 'comment']
        widgets = {
            'book_title': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'comment': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }