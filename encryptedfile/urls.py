from django.urls import path


from .views import FileListView, AddEncryptedField

urlpatterns = [
    path('', FileListView.as_view(), name='file_list'),
    path('new', AddEncryptedField.as_view(), name='add_file'),
]