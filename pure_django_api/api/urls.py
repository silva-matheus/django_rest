from django.urls import path
from . import views

urlpatterns = [
    path('list', views.UpdateModelListAPIView.as_view(), name='list'),
    path('get/<int:id>', views.UpdateModelDetailAPIView.as_view(), name='get'),
]