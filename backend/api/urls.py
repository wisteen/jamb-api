from django.urls import path
from . import views

urlpatterns = [
	path('', views.Jamb_api, name="JAMB API")
]