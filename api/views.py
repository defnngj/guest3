import os
import json
from random import randint
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from guest2.settings import BASE_DIR


def hello_world(request):
    """
    最简单的get请求，返回json格式返回
    """
    return JsonResponse({"code": 10200, "message": "Welcome to API testing"})


def user(request, username):
    """
    通过 URI 传参
    """
    msg = "hello, {}".format(username)
    return JsonResponse({"code": 10200, "message": msg})


def get_user_info(request, uid):
    """
    根据用户id返回数据
    """
    if request.method == "GET":
        user_info = {"id": 1, "name": "tom", "age": 22}
        if uid != 1:
            response = {"code": 10101, "message": "user id null"}
        else:
            response = {"code": 10200, "message": "success", "data": user_info}
        return JsonResponse(response)
    else:
        return JsonResponse({"code": 10101, "message": "request method error"})


def search(request):
    """
    一般GET请求
    """
    if request.method == "GET":
        search_word = request.GET["q"]
        if search_word == "selenium":
            data_list = ["selenium教程", "seleniumhq.org", "selenium环境安装"]
        else:
            data_list = []
        return JsonResponse({"code": 10200, "message": "success", "data": data_list})
    else:
        return JsonResponse({"code": 10101, "message": "request method error"})


def post_login(request):
    """
    请求方法：POST
    参数类型：from-data/x-www-from-urlencode
    """
    if request.method == "POST":
        username = request.POST('username')
        password = request.POST('password')

        if username is None or password is None:
            response = {"code": 10102, "message": "username or passwrord is None"}

        elif username == "" or password == "":
            response = {"code": 10203, "message": "username or passwrord is null"}

        elif username == "admin" and password == "a123456":
            response = {"code": 10200, "message": "login success"}

        else:
            response = {"code": 10104, "message": "username or password error"}
        return JsonResponse(response)
    else:
        return JsonResponse({"code": 10101, "message": "request method error"})


def post_add_user(request):
    """
    请求方法：POST
    参数类型：JSON
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"code": 10105, "message": "format error"})

        try:
            name = data["name"]
            age = data["age"]
            height = data["height"]
        except KeyError:
            response = {"code": 10102, "message": "key null"}
        else:
            if name == "":
                response = {"code": 10103, "message": "name null"}
            elif name == "tom":
                response = {"code": 10104, "message": "name exist"}
            else:
                data = {"name": name, "age": age, "height": height}
                response = {"code": 10200, "message": "add success", "data": data}
        return JsonResponse(response)
    else:
        return JsonResponse({"code": 10101, "message": "request method error"})


def post_header(request):
    """
    请求方法：POST
    带请求提头：Header
    """
    if request.method == 'POST':
        token = request.headers.get("token")
        ct = request.headers.get("Content-Type")
        response = {"code": 10200, "message": "header ok!",
                    "data": {"token": token, "Content-Type": ct}}
        return JsonResponse(response)
    else:
        return JsonResponse({"code": 10101, "message": "request method error"})


def phone(request, pid):
    """
    一个URL, 根据不同的方法做不同的处理
    """
    # 获取数据
    if request.method == 'GET':
        if pid == 1:
            phone_info = {
                "id": pid,
                "name": "小米手机",
                "price": 1999
            }
            response = {"code": 10201, "message": "get success", "data": phone_info}
        else:
            response = {"code": 10101, "message": "The phone id is empty"}
        return JsonResponse(response)

    # 添加数据
    elif request.method == "POST":
        if pid != 1:
            name = request.POST.get('name')
            price = request.POST.get('price')
            phone_info = {
                "id": pid,
                "name": name,
                "price": price
            }
            response = {"code": 10202, "message": "add success", "data": phone_info}
        else:
            response = {"code": 10102, "message": "The pid already exists"}
        return JsonResponse(response)

    # 更新数据
    elif request.method == "PUT":
        if pid == 1:
            name = request.GET.get('name')
            price = request.GET.get('price')
            phone_info = {
                "id": pid,
                "name": name,
                "price": price
            }
            response = {"code": 10203, "message": "update success", "data": phone_info}
        else:
            response = {"code": 10103, "message": "The updated phone id is empty"}
        return JsonResponse(response)

    # 删除数据
    elif request.method == "DELETE":
        if pid == 1:
            response = {"code": 10204, "message": "delete success"}
        else:
            response = {"code": 10104, "message": "The deleted phone id is empty"}
        return JsonResponse(response)


def user_login(request):
    """
    通过Session 记录登录状态
    """
    if request.method == "POST":
        login_username = request.POST.get("username")
        login_password = request.POST.get("password")
        if login_username == '' or login_password == '':
            return JsonResponse({"code": 10201, "message":"username or password null"})
        else:
            user = auth.authenticate(username=login_username, password=login_password)
            if user is not None:
                auth.login(request, user)
                # 将 session 信息记录到浏览器
                request.session['user'] = login_username
                return JsonResponse({"code": 10200, "message": "login success"})
            else:
                return JsonResponse({"code": 10202, "message": "username or password error"})
    else:
        return JsonResponse({"code": 10100, "message": "Request method error"})


@login_required
def user_login_data(request):
    """
    通过Session读取用户数据
    """
    username = request.session.get('user', '') # 读取浏览器 session
    if username == "":
        return JsonResponse({"code": 10200, "message": 'hello, stranger'})
    else:
        return JsonResponse({"code": 10200, "message": 'hello, {}'.format(username)})


def get_activity(request):
    """
    获取抽奖活动
    :return:
    """
    if request.method == "GET":
        activity_info = {"id": 1, "name": "618抽奖活动"}
        return JsonResponse({"code": 10200, "message": "success", "data": activity_info})
    else:
        return JsonResponse({"code": 10101, "message": "request method error"})


def get_user(request):
    """
    获取抽奖用户
    """
    if request.method == "GET":
        user_info = {"id": 1, "name": "张三"}
        return JsonResponse({"code": 10200, "message": "success", "data": user_info})
    else:
        return JsonResponse({"code": 10101, "message": "request method error"})


def get_lucky_number(request):
    """
    获取抽奖号码
    """
    if request.method == "POST":
        activity_id = request.form.get('aid')
        user_id = request.form.get('uid')

        if activity_id is None or user_id is None:
            return JsonResponse({"code": 10102, "message": "username or password is None"})

        elif activity_id == "" or user_id == "":
            return JsonResponse({"code": 10103, "message": "username or password is null"})

        if int(activity_id) != 1:
            return JsonResponse({"code": 10104, "message": "activity id exist"})

        if int(user_id) != 1:
            return JsonResponse({"code": 10105, "message": "user id not exist"})

        number = randint(10000, 99999)
        return JsonResponse({"code": 10200, "message": "Lucky draw number", "data": number})

    else:
        return JsonResponse({"code": 10101, "message": "request method error"})


def upload_file(request):
    """
    文件上传
    """
    if request.method == "POST":
        my_file = request.FILES.get("file", None)
        if not my_file:
            return JsonResponse({"code": 10101, "message": "no files for upload!"})
        destination = open(os.path.join(BASE_DIR, "api/upload", my_file.name), 'wb+')
        for chunk in my_file.chunks():
            destination.write(chunk)
        destination.close()
        return JsonResponse({"code": 10200, "message": "upload success!"})
