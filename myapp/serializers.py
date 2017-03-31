from rest_framework import serializers

from myapp.models import Hymn, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class HymnSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Hymn
        fields = ('id', 'title', 'content', 'number', 'category')
