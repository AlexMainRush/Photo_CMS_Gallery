from ..models.photo_page import PhotoPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PhotoPage)
class PhotoPageAdmin(BasePageAdmin):
    pass
