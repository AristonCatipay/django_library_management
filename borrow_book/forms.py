from django import forms
from .models import Borrow_Book

INPUT_CLASSES = 'rounded-md bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
FOR_IMAGE = 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'

class BorrowBookRequestApproveForm(forms.ModelForm):
    class Meta:
        model = Borrow_Book
        fields = ['pick_up_date', 'return_due_date']
        widgets = {
            'pick_up_date': forms.SelectDateWidget(years=range(2022, 2999), attrs={
                'class': INPUT_CLASSES,
            }),
        }
        