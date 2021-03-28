from django.urls import path
from .views import StaffroomTemplateView 


app_name = "staffroom"

urlpatterns = [
    path("", StaffroomTemplateView.as_view(), name="index"), 
]