from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect

#首页
def index(request):
    return render(request, 'index.html')

# 登录动作处理
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            return render(request, 'index.html', {"error": "usernmae or password null"})

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user) # 验证登录
            response = HttpResponseRedirect('/event_manage/') # 登录成功跳转发布会管理
            request.session['username'] = username    # 将 session 信息写到服务器
            return response
        else:
            return render(request, 'index.html', {"error": "username or password error"})
    else:
        return render(request, 'index.html')


# 发布会管理（登录之后默认页面）
def event_manage(request):
    username = request.session.get('username', '')
    return render(request, "event_manage.html", {"user": username})
