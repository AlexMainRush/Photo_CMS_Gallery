from rest_framework import serializers
from album.models import PhotoPage


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoPage
        fields = '__all__'
