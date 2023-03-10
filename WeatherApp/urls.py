from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls'), name='Home'),
    path('register/', include('register.urls'), name='Register'),
    path("__reload__/", include("django_browser_reload.urls")),
]
