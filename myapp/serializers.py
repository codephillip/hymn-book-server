from rest_framework import serializers

from myapp.models import Hymn


class HymnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hymn
        fields = ('id', 'title', 'content', 'number')
