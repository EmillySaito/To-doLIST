from django.urls import path
from django_dashboard import index

urlpatterns = {
    path('',index, name='index')
}