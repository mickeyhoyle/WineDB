from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.wine_list, name='wine_list'),
    path('winedb/<int:pk>/', views.wine_detail, name='wine_detail'),
    path('winedb/new/', views.add_new_wine, name='add_new_wine'),
    path('winedb/add_bottle/<int:pk>/', views.add_new_bottle, name= 'add_new_bottle'),
	]
