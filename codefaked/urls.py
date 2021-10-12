from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # fix this one to be todo/ soon
    
    path('', include('todo_list.urls')),
]
