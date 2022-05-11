from modeltranslation.translator import TranslationOptions, register
from ..models import PhotoPage


@register(PhotoPage)
class PhotoPageTranslationOptions(TranslationOptions):
    pass
