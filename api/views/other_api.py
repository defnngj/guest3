import os
import json
from random import randint
from django.forms.models import model_to_dict
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from guest3.settings import BASE_DIR
from api.models import User
from api.common import response


def hello_world(request):
    """
    最简单的get请求，返回json格式返回
    """
    return response(10200, "Welcome to API testing")


def user(request, username):
    """
    通过 URI 传参
    """
    msg = "hello, {}".format(username)
    return response(10200, msg)


def get_user_info(request, uid):
    """
    根据用户id返回数据
    """
    if request.method == "GET":
        user_info = {"id": 1, "name": "tom", "age": 22}
        if uid != 1:
            return response(10101, "user id null")
        else:
            return response(10200, data=user_info)
    else:
        return response(10101, "request method error")


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
        return response(10200, data=data_list)
    else:
        return response(10101, "request method error")


def post_login(request):
    """
    请求方法：POST
    参数类型：from-data/x-www-from-urlencode
    """
    if request.method == "POST":
        username = request.POST('username')
        password = request.POST('password')

        if username is None or password is None:
            return response(10102, "username or passwrord is None")

        elif username == "" or password == "":
            return response(10103, "username or passwrord is null")

        elif username == "admin" and password == "a123456":
            return response(10200, "login success")

        else:
            return response(10104, "username or password error")
    else:
        return response(10101, "request method error")


def post_add_user(request):
    """
    请求方法：POST
    参数类型：JSON
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return response(10105, "format error")

        try:
            name = data["name"]
            age = data["age"]
            height = data["height"]
        except KeyError:
            return response(10102, "key null")
        else:
            if name == "":
                return response(10103, "name null")
            elif name == "tom":
                return response(10104, "name exist")
            else:
                data = {"name": name, "age": age, "height": height}
                return response(10200, "add successful", data)
    else:
        return response(10101, "request method error")


def post_header(request):
    """
    请求方法：POST
    带请求提头：Header
    """
    if request.method == 'POST':
        token = request.headers.get("token")
        ct = request.headers.get("Content-Type")
        return response(10200, "header ok!", {"token": token, "Content-Type": ct})
    else:
        return response(10101, "request method error")


def user(request, uid):
    """
    RESTful 风格的接口实现
    实现用户的查询、添加、更新和删除
    /event/1/  = GET
    /event/2/  = POST
    /event/1/  = PUT
    /event/1/  = DELETE
    :param request:
    :param uid:
    :return:
    """
    if request.method == "GET":
        try:
            user = User.objects.get(id=uid)
        except User.DoesNotExist:
            return response(10101, message="用户信息不存在")
        else:
            user_info = model_to_dict(user)
            return response(10200, data=user_info)

    elif request.method == "POST":
        post = json.loads(request.body)
        name = post.get("name")
        age = post.get("age")
        try:
            User.objects.get(id=uid)
        except User.DoesNotExist:
            user = User.objects.create(id=uid, name=name, age=age)
            user_info = model_to_dict(user)
            return response(10200, "add success", user_info)
        else:
            return response(10102, "用户id已存在")

    elif request.method == "PUT":
        put = json.loads(request.body)
        name = put.get("name")
        age = put.get("age")
        try:
            user = User.objects.get(id=uid)
        except User.DoesNotExist:
            return response(10101, "用户信息不存在")
        else:
            user.name = name
            user.age = age
            user.save()
            user_info = model_to_dict(user)
            return response(10200, "update success", user_info)

    elif request.method == "DELETE":
        try:
            user = User.objects.get(id=uid)
        except User.DoesNotExist:
            return response(10101, "用户信息不存在")
        else:
            user.delete()
            return response(10200, "delete success")
    else:
        return response(10101, "request method error")


def user_login(request):
    """
    通过Session 记录登录状态
    """
    if request.method == "POST":
        login_username = request.POST.get("username")
        login_password = request.POST.get("password")
        if login_username == '' or login_password == '':
            return response(10102, "username or password null")
        else:
            user = auth.authenticate(username=login_username, password=login_password)
            if user is not None:
                auth.login(request, user)
                # 将 session 信息记录到浏览器
                request.session['user'] = login_username
                return response(10200, "login success")
            else:
                return response(10103, "username or password error")
    else:
        return response(10101, "request method error")


@login_required
def user_login_data(request):
    """
    通过Session读取用户数据
    """
    username = request.session.get('user', '')   # 读取浏览器 session
    if username == "":
        return response(10200, 'hello, stranger')
    else:
        return response(10200, 'hello, {}'.format(username))


def get_activity(request):
    """
    获取抽奖活动
    :return:
    """
    if request.method == "GET":
        activity_info = {"id": 1, "name": "618抽奖活动"}
        return response(10200, data=activity_info)
    else:
        return response(10101, "request method error")


def get_user(request):
    """
    获取抽奖用户
    """
    if request.method == "GET":
        user_info = {"id": 1, "name": "张三"}
        return response(10200, data=user_info)
    else:
        return response(10101, "request method error")


def get_lucky_number(request):
    """
    获取抽奖号码
    """
    if request.method == "POST":
        activity_id = request.form.get('aid')
        user_id = request.form.get('uid')

        if activity_id is None or user_id is None:
            return response(10102, "username or password is None")

        elif activity_id == "" or user_id == "":
            return response(1010103, "username or password is null")

        if int(activity_id) != 1:
            return response(10104, "activity id exist")

        if int(user_id) != 1:
            return response(10105, "user id not exist")

        number = randint(10000, 99999)
        return response(10200, "Lucky draw number", number)

    else:
        return response(10101, "request method error")


def upload_file(request):
    """
    文件上传
    """
    if request.method == "POST":
        my_file = request.FILES.get("file", None)
        if not my_file:
            return response(10101, "no files for upload!")
        destination = open(os.path.join(BASE_DIR, "api/upload", my_file.name), 'wb+')
        for chunk in my_file.chunks():
            destination.write(chunk)
        destination.close()
        return response(10200, "upload success!")
