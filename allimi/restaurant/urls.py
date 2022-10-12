from django.urls import path
from . import views

app_name = "restaurant" # app_name 설정

urlpatterns = [
    path('sang1F/', views.sang1F, name="sang1F"),
]