from django.urls import path
from api.views import sign_api
from api.views import sign_api_sec
from api.views import other_api

urlpatterns = [

    # 发布会签到系统接口:
    # ex : /api/add_event/
    path('add_event/', sign_api.add_event, name='add_event'),
    # ex : /api/add_guest/
    path('add_guest/', sign_api.add_guest, name='add_guest'),
    # ex : /api/get_event_list/
    path('get_event_list/', sign_api.get_event_list, name='get_event_list'),
    # ex : /api/get_guest_list/
    path('get_guest_list/', sign_api.get_guest_list, name='get_guest_list'),
    # ex : /api/user_sign/
    path('user_sign/', sign_api.user_sign, name='user_sign'),

    # 安全接口
    # ex : /api/sec_get_event_list/
    path('sec_get_event_list/', sign_api_sec.get_event_list, name='get_event_list'),
    # ex : /api/sec_add_event/
    path('sec_add_event/', sign_api_sec.add_event, name='add_event'),
    # ex : /api/sec_get_guest_list/
    path('sec_get_guest_list/', sign_api_sec.get_guest_list, name='get_guest_list'),

    # 更多接口胡学习
    # ex : /api/hello_world/
    path('hello_world/', other_api.hello_world),
    path('user/<slug:username>', other_api.user),
    path('get_user_info/<int:uid>', other_api.get_user_info),
    path('search', other_api.search),
    path('login', other_api.post_login),
    path('add_user', other_api.post_add_user),
    path('header', other_api.post_header),

    # RESTful 风格接口
    path('user/<int:uid>/', other_api.user),

    # session 记录用户状态
    path('user_login', other_api.user_login),
    path('user_login_data', other_api.user_login_data),


    # 接口的依赖
    path('get_activity', other_api.get_activity),
    path('get_user', other_api.get_user),
    path('get_lucky_number', other_api.get_lucky_number),

    # 文件上传
    path('upload_file', other_api.upload_file)

]
