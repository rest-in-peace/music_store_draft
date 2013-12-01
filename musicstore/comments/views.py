# coding: utf-8

from django.contrib.contenttypes.models import ContentType

from rest_framework import generics

from .models import Comment


class BaseCommentListAPIView(generics.ListAPIView):
    '''
    Base CommentList classs to filter comments of a content,
    by it's id and content type

    Subsclass should implement ctype_model attribute
    '''
    model = Comment

    @property
    def ctype_model(self):
        raise NotImplementedError

    def get_queryset(self):
        ctype = ContentType.objects.get_for_model(self.ctype_model)

        qs = super(BaseCommentListAPIView, self).get_queryset()
        qs = qs.filter(content_type=ctype).filter(object_id=self.kwargs['pk'])
        return qs
