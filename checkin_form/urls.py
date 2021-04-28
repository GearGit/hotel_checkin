from django.urls import path
from .views import setCheckInView,homePage

urlpatterns = [
    path('',homePage),
    path('checkin/',setCheckInView)
]
