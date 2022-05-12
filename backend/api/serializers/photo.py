from rest_framework import serializers
from album.models import PhotoPage


class PhotoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PhotoPage
        fields = '__all__'
