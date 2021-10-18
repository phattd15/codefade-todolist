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

def HomePage(request):
    return render(request, 'base/home.html')

def TeamPage(request):
    return render(request, 'base/main2.html')