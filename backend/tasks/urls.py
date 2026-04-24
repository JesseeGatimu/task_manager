from django.urls import path
from .views import TaskListAPI,TaskDetailAPI

urlpatterns=[
    path('tasks/',TaskListAPI.as_view(),name="tasks"),
    path('task-detail/<int:pk>/',TaskDetailAPI.as_view(),name="task-detail"),
]