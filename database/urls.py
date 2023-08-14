from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.wine_list, name='wine_list'),
    path('winedb/new/', views.wine_new, name='wine_new'),
    path('winedb/<int:pk>/', views.wine_detail, name='wine_detail'),
	]
