from django.urls import path

from . import views

urlpatterns = [path("<int:pk>/", views.LocationView.as_view(), name="location")]