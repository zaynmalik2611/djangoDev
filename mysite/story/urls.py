from django.urls import path
from . import views

urlpatterns = [
	path('<int:val>', views.data_stored),
	path('stories/', views.show_stories),
	path('test', views.show_test)
]