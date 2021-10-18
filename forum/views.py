from django.db.models.base import Model
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.forms import ModelForm
from django import forms
from django.views.generic import View
import datetime

from forum.models import Thread, Comment
from django.views.generic.edit import CreateView, DeleteView, FormView
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

def HandlingThread(request, pk):
    thread = Thread.objects.get(id=pk)

    if request.method == 'POST':
        creator = request.POST.get('creator')
        message = request.POST.get('message')
        Comment.objects.create(thread=thread, creator=creator, message=message)

        thread.updated = datetime.datetime.now().time()
        thread.save()

    comments = Comment.objects.filter(thread=thread)

    last_update = thread.updated

    context = {
        'thread': thread,
        'comments': comments,
        'last_update': last_update
    }

    return render(request, 'forum/thread.html', context)
    
    


    
    
    
    




    




