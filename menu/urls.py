from django.urls import path
from . import views


app_name = 'menu'

urlpatterns = [
    path('', views.index),
    path('<str:name_menu>/<str:url_item>/', views.draw_menu),
]
