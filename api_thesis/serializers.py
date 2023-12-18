from rest_framework import serializers
from thesis.models import Thesis, Author, Author_List

class ThesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thesis
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author_List
        fields = '__all__'