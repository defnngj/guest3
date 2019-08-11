from django.http import JsonResponse


def ApiResponse(status=None, message=None, data=[]):
    """
    实现Api的固定格式的返回
    :param status:
    :param message:
    :param data:
    :return:
    """
    if status is None:
        status__ = 10000
    else:
        status__ = 10000 + int(status)

    if message is None:
        message = "successful"

    response_dict = {
        "status": status__,
        "message": message,
        "data": data
    }
    return JsonResponse(response_dict)
