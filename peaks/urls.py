from django.urls import path, include
from .views import PerevalListView, PerevalDetailView, PerevalCreateView


urlpatterns = [
    path('submitData/', PerevalListView.as_view()),
    path('submitData/<int:pk>/', PerevalDetailView.as_view()),
    path('add/', PerevalCreateView.as_view()),

]