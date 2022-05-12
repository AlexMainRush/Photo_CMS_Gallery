from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from album.models import PhotoPage
from ..serializers import PhotoSerializer


class PhotoViewSet(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = PhotoPage.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated,)
