from django.urls import path
from ingest import views


urlpatterns = [
    path('add/', views.create_new_scan)
]