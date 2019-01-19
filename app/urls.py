from django.urls import path, include
from app import views

urlpatterns = [
	path('', views.Home.as_view(), name='home'),
]