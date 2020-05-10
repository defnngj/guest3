"""guest3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,  include
from sign import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # sign 应用
    path('index/', views.index),
    path('', views.index),
    path('accounts/login/', views.index),
    path('login_action/', views.login_action),
    path('event_manage/', views.event_manage),
    path('add_event/', views.add_event),
    path('guest_manage/', views.guest_manage),
    path('add_guest/', views.add_guest),
    path('search_name/', views.search_name),
    path('search_phone/', views.search_phone),
    path('sign_index/<int:event_id>/', views.sign_index),
    #path('sign_index2/<int:event_id>/', views.sign_index2),
    path('sign_index_action/<int:event_id>/', views.sign_index_action),
    path('logout/', views.logout),

    # api 应用
    path('api/', include('api.urls')),
]
