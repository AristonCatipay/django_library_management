from django import forms
from .models import Review

INPUT_CLASSES = 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']
        widgets = {
            'review': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            })
        }
