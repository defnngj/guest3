from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models.event import Event
from sign.models.guest import Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from sign.forms import AddEventForm, AddGuestForm


# 首页
def index(request):
    return render(request, "index.html")


# 登录处理
def login_action(request):
    if request.method == "POST":
        login_username = request.POST.get("username")
        login_password = request.POST.get("password")
        if login_username == '' or login_password == '':
            return render(request, "index.html", {"error": "username or password null"})
        else:
            user = auth.authenticate(
                username=login_username, password=login_password)
            if user is not None:
                auth.login(request, user)  # 验证登录
                response = HttpResponseRedirect('/event_manage/')
                # response.set_cookie('user',login_username, 3600)
                request.session['user'] = login_username  # 将 session 信息记录到浏览器
                return response
            else:
                return render(request, "index.html", {"error": "username or password error"})
    else:
        return render(request, "index.html")


# 发布会管理
@login_required
def event_manage(request):
    #username = request.COOKIES.get('user', '')  # 读取浏览器 cookie
    username = request.session.get('user', '')  # 读取浏览器 session
    events = Event.objects.all()
    return render(request, "event_manage.html", {"user": username, "events": events})

# 发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    #search_name_bytes = search_name.encode(encoding="utf-8")
    events = Event.objects.filter(name__contains=search_name)
    if len(events) == 0:
        return render(request, "event_manage.html", {"user": username,
                                                     "hint": "根据输入的 `发布会名称` 查询结果为空！"})
    return render(request, "event_manage.html", {"user": username, "events": events})


# 添加发布会
def add_event(request):
    username = request.session.get('user', '')

    if request.method == 'POST':
        form = AddEventForm(request.POST)  # form 包含提交的数据
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            limit = form.cleaned_data['limit']
            start_time = form.cleaned_data['start_time']
            status = form.cleaned_data['status']
            if status is True:
                status = 1
            else:
                status = 0

            Event.objects.create(
                name=name, limit=limit, address=address, status=status, start_time=start_time)
            return render(request, "add_event.html", {"user": username, "form": form, "success": "添加发布会成功!"})

    else:
        form = AddEventForm()

    return render(request, "add_event.html", {"user": username, "form": form})


# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guests = Guest.objects.get_queryset().order_by('id')

    paginator = Paginator(guests, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})


# 添加嘉宾
def add_guest(request):
    username = request.session.get('user', '')

    if request.method == 'POST':
        form = AddGuestForm(request.POST)

        if form.is_valid():
            event = form.cleaned_data['event']
            realname = form.cleaned_data['realname']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            sign = form.cleaned_data['sign']
            if sign is True:
                sign = 1
            else:
                sign = 0

            Guest.objects.create(event=event, realname=realname,
                                 phone=phone, email=email, sign=sign)
            return render(request, "add_guest.html", {"user": username, "form": form, "success": "添加嘉宾成功!"})

    else:
        form = AddGuestForm()

    return render(request, "add_guest.html", {"user": username, "form": form})


# 嘉宾手机号的查询
@login_required
def search_phone(request):
    username = request.session.get('user', '')
    search_phone = request.GET.get("phone", "")
    guests = Guest.objects.filter(phone__contains=search_phone)

    if len(guests) == 0:
        return render(request, "guest_manage.html", {"user": username,
                                                     "hint": "根据输入的 `手机号码` 查询结果为空！"})

    paginator = Paginator(guests, 5)  # 少于5条数据不够分页会产生警告
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, "guest_manage.html", {"user": username,
                                                 "guests": contacts,
                                                 "phone": search_phone})

# 签到页面
@login_required
def sign_index(request, event_id):
    print(event_id)
    event = get_object_or_404(Event, id=event_id)
    guest_list = Guest.objects.filter(event_id=event_id)
    guest_data = str(len(guest_list))  # 签到人数
    sign_data = 0                      # 已签到人数
    for guest in guest_list:
        if guest.sign == True:
            sign_data += 1
    return render(request, 'sign_index.html', {'event': event,
                                               'guest': guest_data,
                                               'sign': sign_data})


# 前端签到页面
def sign_index2(request, event_id):
    event_name = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index2.html', {'eventId': event_id,
                                                'eventNanme': event_name})


# 签到动作
@login_required
def sign_index_action(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    guest_list = Guest.objects.filter(event_id=event_id)
    guest_data = str(len(guest_list))
    sign_data = 0
    for guest in guest_list:
        if guest.sign == True:
            sign_data += 1

    phone = request.POST.get('phone', '')

    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'phone error.', 'guest': guest_data, 'sign': sign_data})

    result = Guest.objects.filter(phone=phone, event_id=event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'event id or phone error.', 'guest': guest_data, 'sign': sign_data})

    result = Guest.objects.get(event_id=event_id, phone=phone)

    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': "user has sign in.", 'guest': guest_data, 'sign': sign_data})
    else:
        Guest.objects.filter(event_id=event_id, phone=phone).update(sign='1')
        return render(request, 'sign_index.html', {'event': event, 'hint': 'sign in success!',
                                                   'user': result,
                                                   'guest': guest_data,
                                                   'sign': str(int(sign_data)+1)
                                                   })

# 退出系统
@login_required
def logout(request):
    auth.logout(request)  # 退出登录
    response = HttpResponseRedirect('/index/')
    return response
