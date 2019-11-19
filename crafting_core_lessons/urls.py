from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.StandardList.as_view(), name='standard_list'),
    path('standards/', views.StandardList.as_view(), name='standard_list'),
    path('standard/<int:pk>', views.StandardDetail.as_view(), name='standard_detail'),
    path('lessons/', views.LessonList.as_view(), name='lesson_list'),
    path('lesson/<int:pk>', views.LessonDetail.as_view(), name='lesson_detail'),
    path('lesson/new', views.LessonDetail.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>', views.LessonDetail.as_view(), name='lesson_detail'),
    path('lesson/delete/<int:pk>', views.LessonDetail.as_view(), name='lesson_detail'),
#     path('standard-list/', views.standard_list, name='standard_list'),
#     path('lesson-list/', views.lesson_list, name='lesson_list'),
#     path('lesson-detail/<int:pk>', views.lesson_detail, name='lesson_detail'),
#     path('lesson/new/', views.lesson_create, name='lesson_create'),
#     path('lesson-detail/<int:pk>/edit', views.lesson_edit, name='lesson_edit'),
#     path('lesson-detail/<int:pk>/delete', views.lesson_delete, name='lesson_delete')

]
