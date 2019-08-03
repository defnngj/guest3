from django.urls import path
from api import views

urlpatterns = [
    # learning interface test:
    # ex : /v1/hello_world/
    path('hello_world/', views.hello_world),
    path('user/<slug:username>', views.user),
    path('get_user_info/<int:uid>', views.get_user_info),
    path('search', views.search),
    path('login', views.post_login),
    path('add_user', views.post_add_user),
    path('header', views.post_header),
    path('phone/<int:pid>/', views.phone),

    # session 记录用户状态
    path('user_login', views.user_login),
    path('user_login_data', views.user_login_data),


    # 接口的依赖
    path('get_activity', views.get_activity),
    path('get_user', views.get_user),
    path('get_lucky_number', views.get_lucky_number),

    # 文件上传
    path('upload_file', views.upload_file)

]
