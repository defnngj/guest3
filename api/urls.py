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
]
