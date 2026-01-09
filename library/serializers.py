from rest_framework import serializers
from .models import Category, Book


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "price",
            "published_year",
            "category"
        ]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("manfiy  mumkin emas")
        return value

    def validate_published_year(self, value):
        if value < 1500:
            raise serializers.ValidationError("1500 dan kichik bolmasinn")
        return value
