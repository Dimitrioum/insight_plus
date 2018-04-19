from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='smart_reality_home_page')
]