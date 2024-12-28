from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('sign_in/', views.do_login, name='sign_in'),

    # Administration area   
    path('administration/', views.administration, name='administration'),
    path('administration/users/', views.admin_users, name='admin_users'),
    path('administration/users/load/', views.admin_load_users, name='admin_load_users'),
    path('administration/users_xml/', views.admin_users_xml, name='admin_users_xml'),
    path('administration/users/load_xml/', views.admin_load_users_xml, name='admin_load_users_xml'),
    path('administration/users/load_users/', views.admin_send_users_xml, name='admin_send_users_xml'),
    
    # Normal user area
    path('app/', views.app, name='app'),
    path('app/create/', views.app_create, name='app_create'),
    path('app/create/load_xml/', views.app_load_xml_design, name='app_load_xml_design'),
    path('app/create/image/', views.app_create_image, name='app_create_image'),
    path('app/edit', views.app_edit, name='app_edit'),
    
    path('logout/', views.logout, name='logout')
]