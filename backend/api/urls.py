from django.urls import path
from . import views

urlpatterns = [
	path('', views.Jamb_api, name="JAMB API"),
	path('login', views.login, name="login"),
	path('signup', views.signup, name="signup"),
	path('test_token', views.test_token, name="test_token"),
]