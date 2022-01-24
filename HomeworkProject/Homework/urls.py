from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('report/', views.report),
    path('details/<int:id>/', views.details),
    path('details/<slug:pk>/edit', views.CityUpdateView.as_view(), name="city_edit"),
]