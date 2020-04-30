Django-read-log
---------------
Simple app to log object views can be used in combination with django-simple-history for a full audit solution.
Currently the standard generic class based views: **DetailView**, **UpdateView**, **DeleteView**, **ListView**
are are supported out of the box, since the views deal with displaying objects as part of the functionality.

For DeleteView and UpdateView in most cases you want to display the object (GET request)
before you allow the user to delete/update the object.

For each view the following data is stored in the audit model (ReadLog):

:user: Who view the item, can be an anonymous user.
:content_object: A reference to the viewed object using a generic foreign key, if you delete an object the log entry will still be present.
:operation: What operation triggered the the log entry to be written(detail, list, update, delete).
:logged_at: When was the object viewed.

Usage
=====
Easy to use just in 3 simple steps

1. add the app 'read_log' to INSTALLED_APPS in settings.py
2. run the migration: python manage.py migrate read_log
3. import and use the mixin

.. code-block:: python

    from read_log.view_mixins import ReadLogMixin
    from test_read_log.models import TestModel

    class TestDetailView(ReadLogMixin, DetailView):
        model = TestModel



Presentation not included
_________________________
When audit is needed you normally want to limit the expose of data hench forth no presentation of the ReadLog
is included and if you need it it is up to you to implement it.

.. code-block:: python

    from django.contrib import admin
    from read_log.models import ReadLog

    admin.site.register(ReadLog)