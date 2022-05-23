from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('', views.HomepageView.as_view(), name='homepage'),
]