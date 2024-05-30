from rest_framework import serializers
from myapp.models import Movie, Series, Category, Cast

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True) # this is bonus convert to  string representations
    casts = serializers.StringRelatedField(many=True) # this is bonus convert to  string representations

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'categories', 'casts', 'poster_image']

class SeriesSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    casts = CastSerializer(many=True)

    class Meta:
        model = Series
        fields = ['id', 'title', 'description', 'release_date', 'categories', 'casts', 'poster_image']
