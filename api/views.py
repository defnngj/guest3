import json
from django.http import JsonResponse


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
