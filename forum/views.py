from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView

from forum.models import Thread, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# Create your views here.

from django.http import HttpResponse

def TestingView(request):
    return HttpResponse("this is forum")

class ThreadList(ListView):
    model = Thread
    context_object_name = 'threads'


class CreateThread(CreateView):
    model = Thread
    fields = ['creator', 'title', 'description']
    success_url = reverse_lazy('home')

