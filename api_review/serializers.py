from rest_framework import serializers
from review.models import Review, Reviewed_Item

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['review']

class ReviewedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewed_Item
        fields = ['review', 'book']