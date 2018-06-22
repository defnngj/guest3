from Crypto.Cipher import AES
import base64
import requests
import unittest
import json


class AESGetEventListTest(unittest.TestCase):

    def setUp(self):
        # 字符串自动补全16倍数
        BS = 16
        self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

        self.base_url = "http://127.0.0.1:8000/api/sec_get_guest_list/"
        key = 'W7v4D60fds2Cmk2U'
        self.app_key = key.encode('utf-8')

    def encryptBase64(self,src):
        """
        生成 base64 字符串
        """
        return base64.urlsafe_b64encode(src)

    def encryptAES(self, src, key):
        """
        生成AES密文
        """
        iv = b"1172311105789011"
        cryptor = AES.new(key, AES.MODE_CBC, iv)
        src_str = self.pad(src)
        src_byte = src_str.encode('utf-8')
        ciphertext = cryptor.encrypt(src_byte)  # AES加密
        aes_base64 = self.encryptBase64(ciphertext)  # base64 加密
        print("base64 jiami:")
        print(aes_base64)
        return aes_base64

    def test_aes_interface(self):
        '''test AES interface'''
        payload = {'eid':'', 'phone':''}
        data = json.dumps(payload)
        # 加密
        encoded = self.encryptAES(data, self.app_key).decode()

        r = requests.post(self.base_url, data={"data": encoded})
        result = r.text
        print(result)
        #self.assertEqual(result['status'], 200)
        #self.assertEqual(result['message'], "success")


if __name__ == '__main__':
    unittest.main()
