from django.db import models
from garpix_page.models import BasePage

from album.models import AlbumPage
from album.models.tag import Tag


class PhotoPage(BasePage):
    album = models.ForeignKey(AlbumPage, on_delete=models.CASCADE,
                              related_name="album_photo", verbose_name="Альбом для фото")
    image = models.ImageField(verbose_name="Загружаемое фото", blank=True, null=True)
    photo_tag = models.ManyToManyField(Tag, related_name="tags_photo", verbose_name="Теги для фото")
    template = "pages/photo.html"

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ("-created_at",)
