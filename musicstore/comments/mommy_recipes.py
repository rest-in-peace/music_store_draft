# coding: utf-8

from django.contrib.contenttypes.models import ContentType

from model_mommy.recipe import Recipe

from albums.models import Album
from .models import Comment


album_comment = Recipe(Comment,
    content_type=ContentType.objects.get_for_model(Album),
)
