from rest_framework import serializers
from book.models import Book, Author, Author_List
from review.models import Reviewed_Item

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author_List
        fields = '__all__'

class ReviewedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewed_Item
        fields = '__all__'