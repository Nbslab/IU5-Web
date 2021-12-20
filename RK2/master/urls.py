from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('PC/', views.pcs),
    path('Program/', views.programs),
    path('PC/<int:id>/', views.pc),
    path('Program/<int:id>/', views.program),
]