from rest_framework import viewsets

from album.models import AlbumPage
from ..serializers import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = AlbumPage.objects.all()
    serializer_class = AlbumSerializer
