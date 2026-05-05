from django.contrib import admin
from django.urls import path, include
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('my_app.urls')),
    path('', views.index, name='index'),  # Add this line to handle the root path
]