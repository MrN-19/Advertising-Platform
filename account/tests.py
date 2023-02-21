from django.test import TestCase,Client
from django.contrib.auth.models import User


class UserRegisterTestCase(TestCase):

    SUCCESS_STATUS:int = 200
    CLIENT_ERROR:int = 400

    def setUp(self) -> None:
        self.__example_email:str = "test@gmail.com"
        self.__example_password:str = "adminadmin"
        self.__example_re_password:str = "adminadmin"
        self.__another_password:str = "admiadmin1234"
        
        self.__client = Client(enforce_csrf_checks=True)

    def test_register_successfully(self):
        data = {
            "email" : self.__example_email,
            "password" : self.__example_password,
            "re_password" : self.__example_re_password
        }
        response = self.__client.post("/register",data = data)
        self.assertEqual(response.status_code,self.SUCCESS_STATUS)

    def test_register_without_email(self):
        data = {
            "email" : "",
            "password" : self.__example_password,
            "re_password" : self.__example_re_password
        }
        response = self.__client.post("/register",data = data)
        self.assertEqual(response.status_code,self.CLIENT_ERROR)

    def test_register_without_password(self):
        data = {
            "email" : self.__example_email,
            "password" : "",
            "re_password" : self.__example_re_password
        }
        response = self.__client.post("/register",data = data)
        self.assertEqual(response.status_code,self.CLIENT_ERROR)

    def test_register_without_re_password(self):
        data = {
            "email" : self.__example_email,
            "password" : self.__example_password,
            "re_password" : "",
        }
        response = self.__client.post("/register",data = data)
        self.assertEqual(response.status_code,self.CLIENT_ERROR)

    def test_register_not_same_password(self):
        data = {
            "email" : self.__example_email,
            "password" : self.__example_password,
            "re_password" : self.__another_password
        }
        response = self.__client.post("/register",data = data)
        self.assertEqual(response.status_code,self.CLIENT_ERROR)
    
    def test_register_lower_password_characters(self):
        data = {
            "email" : self.__example_email,
            "password" : "123",
            "re_password" : "123",
        }
        response = self.__client.post("/register",data = data)
        self.assertEqual(response.status_code,self.CLIENT_ERROR)

    

class UserLoginTestCase(TestCase):

    SUCCESS_STATUS:int = 200
    CLIENT_ERROR:int = 400

    def setUp(self) -> None:
        self.__example_email:str = "test@gmail.com"
        self.__example_password:str = "adminadmin"
        self.__example_re_password:str = "adminadmin"

        User.objects.create_user(username = self.__example_email,
                                email = self.__example_email,
                                password=self.__example_password)
        
        
        self.__client = Client(enforce_csrf_checks=True)

    def test_login_successfully(self):
        data = {
            "email" : self.__example_email,
            "password" : self.__example_password
        }
        response = self.__client.post("/login",data = data)
        self.assertEqual(response.status_code,self.SUCCESS_STATUS)
    
    def test_login_without_email(self):
        data = {
            "email" : "",
            "password" : self.__example_password
        }
        response = self.__client.post("/login",data = data)
        self.assertEqual(response.status_code,self.CLIENT_ERROR)

    def test_login_without_password(self):
        data = {
            "email" : self.__example_email,
            "password" : "",
        }
        response = self.__client.post("/login",data = data)
        self.assertEqual(response.status_code,self.CLIENT_ERROR)

    def test_login_lower_password(self):
        data = {
            "email" : self.__example_email,
            "password" : "123",
        }
        response = self.__client.post("/login",data = data)
        self.assertEqual(response.status_code,self.CLIENT_ERROR)