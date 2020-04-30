from django.urls import path
from django.contrib import admin
from test_read_log.views import TestDetailView, TestUpdateView, TestDeleteView, TestListView, \
    TestCustomListView, TestCustomDetailView

urlpatterns = [
    path('test/<int:pk>/', TestDetailView.as_view(), name='test-detail'),
    path('update/<int:pk>/', TestUpdateView.as_view(), name='test-update'),
    path('delete/<int:pk>/', TestDeleteView.as_view(), name='test-delete'),
    path('list/', TestListView.as_view(), name='test-list'),
    path('custom-list/', TestCustomListView.as_view(), name='custom-test-list'),
    path('custom-detail/<int:pk>/', TestCustomDetailView.as_view(), name='custom-test-detail'),
    path('admin/', admin.site.urls),
]

