from django.urls import path
from api import views

urlpatterns = [
    # learning interface test:
    # ex : /v1/hello_world/
    path('hello_world/', views.hello_world),
    path('user/<slug:username>', views.user),
    path('get_user_info/<int:uid>', views.get_user_info),

]