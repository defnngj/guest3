from django.urls import path
from sign import views_api, views_api_sec


urlpatterns = [
    # guest system interface:
    # ex : /api/add_event/
    path('add_event/', views_api.add_event, name='add_event'),
    # ex : /api/add_guest/
    path('add_guest/', views_api.add_guest, name='add_guest'),
    # ex : /api/get_event_list/
    path('get_event_list/', views_api.get_event_list, name='get_event_list'),
    # ex : /api/get_guest_list/
    path('get_guest_list/', views_api.get_guest_list, name='get_guest_list'),
    # ex : /api/user_sign/
    path('user_sign/', views_api.user_sign, name='user_sign'),
	# security interface:
    # ex : /api/sec_get_event_list/
    path('sec_get_event_list/', views_api_sec.get_event_list, name='get_event_list'),
    # ex : /api/sec_add_event/
    path('sec_add_event/', views_api_sec.add_event, name='add_event'),
    # ex : /api/sec_get_guest_list/
    path('sec_get_guest_list/', views_api_sec.get_guest_list, name='get_guest_list'),
]
