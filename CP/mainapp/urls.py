from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('rank/', views.rank, name='rank'),
    path('album/', views.album, name='album'),
    path('create_album/', views.create_album, name='create_album'),
    path('delete_album/', views.delete_album, name='delete_album'),
    path('search/', views.search, name='search'),
]