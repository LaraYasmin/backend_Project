from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name='store'
urlpatterns = [
    path('', views.all_products,name='all_products'),
]