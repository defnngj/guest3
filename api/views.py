from django.shortcuts import render
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
