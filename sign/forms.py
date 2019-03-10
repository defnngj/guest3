from django import forms
from django.forms import ModelForm
from sign.models.event import Event
from sign.models.guest import Guest


# 添加发布会表单
class AddEventForm(forms.Form):
    name = forms.CharField(max_length=100)            # 发布会标题
    limit = forms.IntegerField()                      # 限制人数
    status = forms.BooleanField(required=False)       # 状态
    address = forms.CharField(max_length=200)         # 地址
    start_time = forms.DateTimeField()                # 发布会时间


# 添加嘉宾
class AddGuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['event', 'realname', 'phone', 'email', 'sign']
