from django.urls import path 
from . import views  # convention / 사실 그냥 import 해도 됨 

urlpatterns = [
    path('num/push/', views.num_push),
    path('num/pull/', views.num_pull),

    path('static_example/', views.static_example),

    path('lotto_pick/', views.lotto_pick),
    path('lotto_result/', views.lotto_result),
    path('lotto_error/', views.lotto_error),
    path('result/', views.result),
    path('search/', views.search),
    
    path('lotto/', views.lotto),
    path('isitbirthday/<str:month>/<str:day>/', views.isitbirthday),
    path('template_language/', views.template_language),
    path('times/<int:num1>and<int:num2>/', views.times),  # <int:num1>/<int:num2>/
    path('<str:word>/', views.name),
    path('greeting/<str:name>/', views.greeting),
    path('image/', views.image),
    path('dinner/<str:name>', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),  # 특정 주소에서 실행될 함수를 설정 
]
