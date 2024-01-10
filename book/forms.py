from django import forms
from .models import Book, Author, Author_List

INPUT_CLASSES = 'rounded-r-lg bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
SELECT_AREA = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
TEXT_AREA = 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
FOR_IMAGE = 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'
CHECKBOX = 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'cover_image', 'overview_image', 'table_of_contents_image', 'isbn_number', 'date_published', 'inventory', 'rack_number', 'rack_level_number']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'cover_image': forms.FileInput(attrs={
                'class': FOR_IMAGE,
            }),
            'overview_image': forms.FileInput(attrs={
                'class': FOR_IMAGE,
            }),
            'table_of_contents_image': forms.FileInput(attrs={
                'class': FOR_IMAGE,
            }),
            'isbn_number': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'date_published': forms.SelectDateWidget(years=range(1500, 2999), attrs={
                'class': SELECT_AREA,
            }),
            'inventory': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'rack_number': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'rack_level_number': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'author_image']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'last_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'author_image': forms.FileInput(attrs={
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