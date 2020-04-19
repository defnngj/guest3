# guest3

基于Django的简易发布会签到系统（基于 Dango3.0）。

__注：本项目与书上的代码会有一些差异。__

### Python版本与依赖库：
  * python 3.6 + : https://www.python.org/
  * Django 3.0 + : https://www.djangoproject.com/
  * PyMySQL 0.8.0: https://github.com/PyMySQL/PyMySQL
  * pycryptodome 3.7.3：https://github.com/Legrandin/pycryptodome 

#### 提供接口

|接口| URL | 请求方式|
|:---|:---|:---|
|添加发布会接口 | http://127.0.0.1:8000/api/add_event/ | POST |
|查询发布会接口 | http://127.0.0.1:8000/api/get_event_list/ | GET |
|添加嘉宾接口 | http://127.0.0.1:8000/api/add_guest/ | POST |
|查询嘉宾接口 | http://127.0.0.1:8000/api/get_guest_list/ | GET |
|嘉宾签到接口 | http://127.0.0.1:8000/api/user_sign/ | GET |
