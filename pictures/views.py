from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Picture
from django.utils import timezone

class PictureList(ListView):
    model = Picture
    # queryset = Picture.objects.filter(title__icontains="nature")
    template_name = 'pictures/my_picture_list.html'
    context_object_name = 'pics_list'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['today'] = timezone.now()
    #     return context


class PictureDetail(DetailView):
    model = Picture
    context_object_name = "pic"


class PictureCreate(CreateView):
    model = Picture
    fields = ['title', 'picture', 'description']
    success_url = reverse_lazy('picture_list')


class PictureUpdate(UpdateView):
    model = Picture
    fields = ['title', 'picture', 'description']
    success_url = reverse_lazy('picture_list')


class PictureDelete(DeleteView):
    model = Picture
    success_url = reverse_lazy('picture_list')
