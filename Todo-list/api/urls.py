
from django.urls import path, include
from .views import TaskViewSet

urlpatterns = [
    path('apitask', TaskViewSet.as_view()),
]