from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from read_log.models import ReadLog
from test_read_log.models import TestModel


class ReadLogMixinTestCase(TestCase):
    def setUp(self) -> None:
        self.object = TestModel.objects.create()
        self.username = 'test'
        self.password = 'test'
        User = get_user_model()
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)
        User.objects.create_user(username='secondary', password='secret')
        for i in range(0,5):
            TestModel.objects.create(test=str(i))

    def test_detail_view(self):
        url = reverse('test-detail', args=(self.object.id,))
        response = self.client.get(url)
        self.assertEqual(ReadLog.objects.count(), 1)
        self.assertCountEqual(ReadLog.objects.all(), self.object.logs.all())
        read_log = ReadLog.objects.first()
        self.assertEqual(read_log.user, self.user)
        self.assertEqual(read_log.operation, 'detail')
        self.assertEqual(read_log.content_object, response.context['object'])

    def test_update_view(self):
        url = reverse('test-update', args=(self.object.id,))
        response = self.client.get(url)
        self.assertEqual(ReadLog.objects.count(), 1)
        self.assertCountEqual(ReadLog.objects.all(), self.object.logs.all())
        read_log = ReadLog.objects.first()
        self.assertEqual(read_log.user, self.user)
        self.assertEqual(read_log.operation, 'update')

    def test_delete_view(self):
        url = reverse('test-delete', args=(self.object.id,))
        response = self.client.get(url)
        self.assertEqual(ReadLog.objects.count(), 1)
        self.assertCountEqual(ReadLog.objects.all(), self.object.logs.all())
        read_log = ReadLog.objects.first()
        self.assertEqual(read_log.user, self.user)
        self.assertEqual(read_log.operation, 'delete')

    def test_list_view(self):
        url = reverse('test-list')
        response = self.client.get(url)
        self.assertEqual(ReadLog.objects.count(), 3)  # paginated by 3
        shown_items = []
        for instance in ReadLog.objects.all():
            self.assertEqual(instance.user, self.user)
            self.assertEqual(instance.operation, 'list')
            shown_items.append(instance.content_object)
        # check that the logged items are equal the shown items
        self.assertCountEqual(shown_items, response.context['object_list'])

    def test_custom_operation_for_list(self):
        url = reverse('custom-test-list')
        response = self.client.get(url)
        self.assertEqual(ReadLog.objects.count(), 2)  # paginated by 2
        shown_items = []
        for instance in ReadLog.objects.all():
            self.assertEqual(instance.user, self.user)
            self.assertEqual(instance.operation, 'filtering')
            shown_items.append(instance.content_object)
        # check that the logged items are equal the shown items
        self.assertCountEqual(shown_items, response.context['object_list'])

    def test_custom_operation_for_detail(self):
        url = reverse('custom-test-detail', args=[self.object.id])
        response = self.client.get(url)
        self.assertEqual(ReadLog.objects.count(), 1)
        self.assertCountEqual(ReadLog.objects.all(), self.object.logs.all())
        read_log = ReadLog.objects.first()
        self.assertEqual(read_log.user, self.user)
        self.assertEqual(read_log.operation, 'not-detail')
        self.assertEqual(read_log.content_object, response.context['object'])