from django.urls import path
from .views import *

urlpatterns = [
    path('',InitialView.as_view()),
    path('checkin',CheckInView.as_view()),
    path('home',HomeView.as_view()),
    path('update/<int:id>',UpdateView.as_view()),
    path('delete/<int:id>',DeleteView.as_view()),
]
