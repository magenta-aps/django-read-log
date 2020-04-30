Django-read-log
---------------
Simple app to log every time an object is displayed, can be used in combination with django-simple-history for a full audit solution.
Currently the standard generic class based views: **DetailView**, **UpdateView**, **DeleteView**, **ListView**
are are supported out of the box, since the views deal with displaying objects as part of the functionality.
For DeleteView and UpdateView in most cases you want to display the object (GET request)
before you allow the user to delete/update the object.

Other custom views can most likely be supported see `Using django-read-log in combination with unsupported views`_

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

Customizing logged operations
_____________________________
By default the following views maps to the following operations.

:DetailView: detail
:UpdateView: update
:ListView: list
:Delete: delete

This can be changed by setting the **log_operations** attribute to a string of you choice

.. code-block:: python

    from read_log.view_mixins import ReadLogMixin
    from test_read_log.models import TestModel

    class TestDetailView(ReadLogMixin, DetailView):
        log_operation = 'my_choice'
        model = TestModel

Using django-read-log in combination with unsupported views
___________________________________________________________
Because the view mixin hooks into the **get_context_data** view function it should be possible to add the mixin to
unsupported views as long as they either implement or inherit the get_context_data function
(eg. from SingleObjectMixin or MultipleObjectMixin) and define the class attribute **'log_operation'** to the string
you want to have logged as the operations field.

Presentation not included
_________________________
When audit is needed you normally want to limit the expose of data hench forth no presentation of the ReadLog
is included and if you need a way to display the Readlog it is up to you to implement it.

.. code-block:: python

    from django.contrib import admin
    from read_log.models import ReadLog

    admin.site.register(ReadLog)