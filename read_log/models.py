from django.db import models
from uuid import uuid4
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from django.views.generic import DetailView, DeleteView, UpdateView, ListView

operation_choices = (
    ('detail', _('Detail view, directly targeted')),
    ('list', _('List view, was part of the result list for a list/search view')),
    ('update', _('Update view, the object was displayed as part of editing the object.')),
    ('delete', _('Delete view, the object was displayed as part of deleting the object.'))
)


class ReadLog(models.Model):
    uuid = models.UUIDField(editable=False, blank=True, primary_key=True, default=uuid4)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_uuid = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_uuid')
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    operation = models.TextField(choices=operation_choices)
    logged_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def generate_read_log_entries(cls, view, content_objects, user):
        """
        :param view: instance of the view
        :param content_objects: queryset or list of objects that needs to be logged
        :param user: user or anon user that needs to be logged
        """
        operation = getattr(view, 'log_operation', None)
        # allows overriding the log_operation directly on the view.
        if operation is None:
            if isinstance(view, DetailView):
                operation = 'detail'
            elif isinstance(view, UpdateView):
                operation = 'update'
            elif isinstance(view, DeleteView):
                operation = 'delete'
            elif isinstance(view, ListView):
                operation = 'list'
            else:
                operation = 'unknown'
        
        for content_object in content_objects:
            cls.objects.create(content_object=content_object, operation=operation, user=user)
