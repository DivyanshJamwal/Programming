from django.urls import path
from . import views

handler404 = 'my_app.views.handler404'
handler500 = 'my_app.views.handler500'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('form1/', views.form1),
    path('destinations/', views.destinations_list, name='destinations_list'),
    path('destinations/<int:destination_id>/', views.destination_detail, name='destination_detail') # New form view
]
