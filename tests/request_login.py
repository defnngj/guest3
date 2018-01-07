import requests

login = requests.Session()

user = {"username":"admin", "password":"admin123456"}
r = login.post("http://127.0.0.1:8000/login_action/", data=user)
r = login.get("http://127.0.0.1:8000/event_manage/")
print(r.text)
