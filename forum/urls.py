from django.http import HttpResponse
from django.urls import path
from .views import CreateThread, TestingView, ThreadList
urlpatterns = [
    path('', ThreadList.as_view(), name="home"),
    path('create-thread/', CreateThread.as_view(), name="create_thread"),
]