from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from read_log.view_mixins import ReadLogMixin
from test_read_log.models import TestModel


class TestDetailView(ReadLogMixin, DetailView):
    model = TestModel


class TestUpdateView(ReadLogMixin, UpdateView):
    template_name = 'test_read_log/testmodel_detail.html'
    model = TestModel
    fields = ('test', )


class TestDeleteView(ReadLogMixin, DeleteView):
    template_name = 'test_read_log/testmodel_detail.html'
    model = TestModel
    fields = ('test', )


class TestListView(ReadLogMixin, ListView):
    template_name = 'test_read_log/testmodel_detail.html'
    model = TestModel
    paginate_by = 3


class TestCustomListView(ReadLogMixin, ListView):
    log_operation = 'filtering'
    template_name = 'test_read_log/testmodel_detail.html'
    model = TestModel
    paginate_by = 2


class TestCustomDetailView(ReadLogMixin, DetailView):
    model = TestModel
    log_operation = 'not-detail'