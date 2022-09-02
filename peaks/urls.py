from django.urls import path, include
from .views import PerevalListView, PerevalDetailView


urlpatterns = [
    path('pereval/', PerevalListView.as_view()),
    path('pereval/<int:pk>/', PerevalDetailView.as_view()),
]