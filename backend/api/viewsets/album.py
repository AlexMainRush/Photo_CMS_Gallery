from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from album.models import AlbumPage, PhotoPage
from ..serializers import AlbumSerializer


class AlbumViewSet(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = AlbumPage.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=False)
    def photo_count(self, request):
        count = PhotoPage.objects.all().count()
        return Response({'photo_count': count})

