from django.urls import path
from .views import AdminDashboardView, HomeDashboardView

app_name = 'dashboard'
urlpatterns = [
    path('', HomeDashboardView.as_view(), name='home'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
]
