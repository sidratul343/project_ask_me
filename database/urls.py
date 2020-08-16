from django.urls import path
from django.conf.urls import url
from . import index

urlpatterns = [
    path('',index.front,name='front'),
    path('admin/',admin.site.urls)
]