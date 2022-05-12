from rest_framework import serializers
from album.models import AlbumPage


class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = AlbumPage
        fields = '__all__'


class AlbumTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPage
        fields = ('title', )
        read_only_fields = ('title', )

