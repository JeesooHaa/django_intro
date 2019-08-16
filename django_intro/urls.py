"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    # path('사용자가 접속하는 경로', 실행할 함수)
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
    path('admin/', admin.site.urls),
]
