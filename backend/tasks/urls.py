from django.urls import path
from .views import TaskListCreateAPI,TaskDetailAPI

urlpatterns=[
    path('',TaskListCreateAPI.as_view(),name="task-list"),
    path('<int:pk>/',TaskDetailAPI.as_view(),name="task-detail"),
]