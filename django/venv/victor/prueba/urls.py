from django.urls import path
from . import views

urlpatterns = [
    path('show-tables/', views.show_tables, name='show_tables'),
]