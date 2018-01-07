from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

#fe0yi8xkqdnc5szgqny35pczg9v9t68l

# 首页
def index(request):
    return render(request,"index.html")

# 登录处理
def login_action(request):
    if request.method == "POST":
        login_username = request.POST.get("username")
        login_password = request.POST.get("password")
        if login_username == '' or login_password == '':
            return render(request,"index.html", {"error":"username or password null"})
        else:
            user = auth.authenticate(username = login_username, password = login_password)
            if user is not None:
                auth.login(request, user) # 验证登录
                response = HttpResponseRedirect('/event_manage/')
                # response.set_cookie('user',login_username, 3600)
                request.session['user'] = login_username # 将 session 信息记录到浏览器
                return response
            else:
                return render(request,"index.html", {"error":"username or password error"})
    else:
        return render(request, "index.html")


# 发布会管理
@login_required
def event_manage(request):
    #username = request.COOKIES.get('user', '')  # 读取浏览器 cookie
    username = request.session.get('user', '') # 读取浏览器 session
    return render(request, "event_manage.html", {"user": username})


# 退出系统
@login_required
def logout(request):
    auth.logout(request) #退出登录
    response = HttpResponseRedirect('/index/')
    return response



'''
0、通过表单或链接
<a href="/index/">Index</a>
1、指定路径
http://127.0.0.1:8000/index/
2、打开url配置文件 settings.py
ROOT_URLCONF = 'guest2.urls'
3、urls.py 找到 views
path('index/', views.index),
4、index 函数返回HttpResponse 对应
'''
