# Python Test lib 
import unittest
from Models.processLogin import LoginForm
from Models.editLevel import fetchPassword
from flask import Flask
from CoolMotor import app
import time


class TestLoginForm(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    # checks if LoginForm returns the correct class
    def test_checkFormClass(self):
        form_class = LoginForm()
        self.assertIsInstance(form_class, LoginForm)

    # tests if login page is working properly
    def test_login_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    # helper function to send login POST request
    def login(self, password):
        response = self.client.post('/login', data={
                'password': password
            })
        return response

    # tests for login failure.
    def test_loginFailure(self):
        res = self.login('rubbishpassword')
        self.assertIn(b"Wrong Password!", res.data)

    # tests for login success.
    def test_loginSuccess(self):
        password = str(fetchPassword())[3:-4]
        res = self.login(password)
        self.assertIn(b"/edit_level", res.data)

    # tests the login bruteforcer.
    def test_loginBrute(self):
        for i in range(5):
            res = self.login('rubbishpassword')
        self.assertIn(b"Too many incorrect logins incident!", res.data)

    # tests the login bruteforcer timeout
    def test_loginBruteReset(self):
        for i in range(5):
            res = self.login('rubbishpassword')
        self.assertIn(b"Too many incorrect logins incident!", res.data)

        time.sleep(10)
        res = self.login('rubbishpassword')
        self.assertNotIn(b"Too many incorrect logins incident!", res.data)


if __name__ in '__main__':
    unittest.main()
