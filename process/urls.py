from django.urls import path
from process import views


urlpatterns = [
    path('delete/', views.get_scan_by_id)
]