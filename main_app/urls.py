from django.conf.urls import url
from . import views

urlpatterns = [
	url('', views.ListDest.as_view()),
	url('<int:pk>/', views.DetailDest.as_view()),
]