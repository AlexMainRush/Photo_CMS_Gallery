from rest_framework import serializers
from album.models import AlbumPage


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPage
        fields = '__all__'
