from read_log.models import ReadLog
from itertools import chain


class ReadLogMixin(object):
    log_operation = None

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ReadLogMixin, self).get_context_data(*args, object_list=object_list, **kwargs)
        objects = context.get('object_list', [])
        instance = context.get('object', None)
        if instance:
            if objects:
                objects = chain(objects, instance)
            else:
                objects = [instance]

        if objects:
            ReadLog.generate_read_log_entries(self, objects, self.request.user)

        return context
