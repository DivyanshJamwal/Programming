from django.contrib import admin
from django.urls import path, include
from my_app import urls as my_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(my_app_urls)),
]
