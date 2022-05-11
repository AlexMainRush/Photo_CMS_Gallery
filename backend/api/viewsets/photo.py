from rest_framework import viewsets

from album.models import PhotoPage
from ..serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = PhotoPage.objects.all()
    serializer_class = PhotoSerializer
