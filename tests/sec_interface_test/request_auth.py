import requests
import unittest

class GetEventListTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/sec_get_event_list/"

    def test_get_event_list_auth_null(self):
        ''' 认证参数为空 '''
        r = requests.get(self.base_url, params={'eid':1})
        result = r.json()
        self.assertEqual(result['status'], 10011)
        self.assertEqual(result['message'], 'user auth null')


    def test_get_event_list_auth_error(self):
        ''' 认证参数错误 '''
        r = requests.get(self.base_url, params={'eid':1}, auth=('error', '123'))
        result = r.json()
        self.assertEqual(result['status'], 10012)
        self.assertEqual(result['message'], 'user auth fail')

    def test_get_event_list_auth_ok(self):
        ''' 认证参数通过 '''
        user_auth = ('admin', 'admin123456')
        r = requests.get(self.base_url, params={'eid':''}, auth=user_auth)
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

if __name__ == '__main__':
    unittest.main()
