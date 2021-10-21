from django.urls import path
from status import views


urlpatterns = [
    path('scan/<id>/', views.get_scan_by_id)
]