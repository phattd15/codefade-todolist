from django.http import HttpResponse
from django.urls import path
from .views import *
urlpatterns = [
    path('', ThreadList.as_view(), name="home"),
    path('create-thread/', CreateThread.as_view(), name="create_thread"),
    path('thread/<int:pk>/', HandlingThread, name="thread")
]