from django.core.exceptions import ValidationError
from django.db import models
from garpix_page.models import BasePage

from album.models import AlbumPage
from album.models.tag import Tag
from user.models import User


def validate_file_size(value):
    file_size = value.size
    if file_size > 1024 * 1024 * 5:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value


class PhotoPage(BasePage):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_photo", verbose_name="Пользователь альбома", blank=True, null=True)
    album = models.ForeignKey(AlbumPage, on_delete=models.CASCADE,
                              related_name="album_photo", verbose_name="Альбом для фото")
    image = models.ImageField(validators=[validate_file_size], verbose_name="Загружаемое фото", blank=True, null=True)
    #  photo_small = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),ResizeToFill(150, 150)], format='JPEG', options={'quality': 90})
    photo_tag = models.ManyToManyField(Tag, related_name="tags_photo", verbose_name="Теги для фото")
    template = "pages/photo.html"

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ("-created_at",)

