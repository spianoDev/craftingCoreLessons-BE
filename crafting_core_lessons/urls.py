from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.StandardList.as_view(), name='standard_list'),
    path('standards/', views.StandardList.as_view(), name='standard_list'),
    path('standard/<int:pk>', views.StandardDetail.as_view(), name='standard_detail'),
    path('lessons/', views.LessonList.as_view(), name='lesson_list'),
    path('lesson/<int:pk>', views.LessonDetail.as_view(), name='lesson_detail'),
]
