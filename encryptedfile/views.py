from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
# Create your views here.
from .models import EncryptedFile
from .forms import EncryptedFileForm

class FileListView(LoginRequiredMixin,ListView):
    """ list view of encrypted files """
    model = EncryptedFile
    template_name="encryptedfile/file_list.html"
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(user = self.request.user)
        return queryset


class AddEncryptedField(LoginRequiredMixin,CreateView):
    """ create view for uploading files """
    template_name='encryptedfile/add_file.html'
    form_class = EncryptedFileForm
    success_url=reverse_lazy('file_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())