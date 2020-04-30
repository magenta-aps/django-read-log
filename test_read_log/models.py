from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from read_log.models import ReadLog


class TestModel(models.Model):
    id = models.AutoField(primary_key=True)
    test = models.CharField(max_length=2)
    logs = GenericRelation(ReadLog, object_id_field='object_uuid')

    class Meta:
        ordering = ('test', )
