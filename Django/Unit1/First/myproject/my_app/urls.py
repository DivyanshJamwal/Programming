from django.urls import path,re_path
from . import views

handler404 = 'my_app.views.handler404'
handler500 = 'my_app.views.handler500'

urlpatterns = [
        path('', views.default_home),
        path('hello/', views.hello),
        path('menuitems/', views.menuitems),
        path('greet/<str:name>/', views.greet),
        path('menuitems1/<str:dish>/', views.menuitems1),
        path('menuitems2/<str:dish>/', views.menuitems2),
        path('queryParameter/', views.queryParameter),
        path('err404/', views.handler404),
        path('err500/', views.handler500),
        re_path(r'^user/(?P<username>[a-zA-Z]*)/$',views.user_profile),       # +means required, * means optional
        re_path(r'^userNumber/(?P<number>[0-9]{3})/$',views.user_profile_number),
        path('form1/', views.form1),
        path('destinations/', views.destinations_list, name='destinations_list'),
        path('destinations/<int:destination_id>/', views.destination_detail, name='destination_detail'),
        path('set_cookie/', views.set_cookie, name='set_cookie'),
        path('get_cookie/', views.get_cookie, name='get_cookie'),
        path('delete_cookie/', views.delete_cookie, name='delete_cookie'),
        path('set_session/', views.set_session, name='set_session'),
        path('get_session/', views.get_session, name='get_session'),
        path('delete_session/', views.delete_session, name='delete_session'),
        path('my_model/', views.my_model_list, name='my_model_list'),
        path('my_model/create/', views.my_model_create, name='my_model_create'),
        path('my_model/update/<int:id>/', views.my_model_update, name='my_model_update'),
    ]