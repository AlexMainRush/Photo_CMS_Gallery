from rest_framework import routers

from api.viewsets import AlbumViewSet, PhotoViewSet

api_router = routers.DefaultRouter()
api_router.register('album', AlbumViewSet)
api_router.register('photo', PhotoViewSet)

urlpatterns = []
urlpatterns += api_router.urls
