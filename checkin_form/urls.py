from django.urls import path
from .views import HomeView, CheckInView,InitialView

urlpatterns = [
    path('',InitialView.as_view()),
    path('checkin',CheckInView.as_view()),
    path('home',HomeView.as_view()),
]
