from django.db import models
from garpix_page.models import BasePage

from user.models import User


class AlbumPage(BasePage):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_album", verbose_name="Пользователь альбома")
    template = "pages/album.html"

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        ordering = ("-created_at",)
