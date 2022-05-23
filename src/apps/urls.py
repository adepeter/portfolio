from django.urls import path, include

app_name = 'apps'

urlpatterns = [
    path('home/', include('apps.home.urls', namespace='home')),
]