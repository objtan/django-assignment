from xml.etree.ElementInclude import include
from django.urls import path, include

from . import views

app_name = 'asigm'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:person_id>/', views.detail, name='detail'),
    path('adduser/', views.adduser, name='adduser'),
    path('delete/<int:person_id>', views.delete, name='delete'),
]