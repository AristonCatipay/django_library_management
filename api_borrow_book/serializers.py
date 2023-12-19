from rest_framework import serializers
from borrow_book.models import Borrow_Book

class BorrowBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow_Book
        fields = '__all__'

class BorrowRequestApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow_Book
        fields = ['pick_up_date']