from django.urls import path 
from . import views  # convention / 사실 그냥 import 해도 됨 

# /utilities/
urlpatterns = [
    path('index/', views.index),
]
