from django.urls import path

from mainapp.views import index, contacts

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
]

