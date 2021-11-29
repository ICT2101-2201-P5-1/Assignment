# Python Test lib 
import unittest
from Models.processLogin import LoginForm
from wtforms_test import FormTestCase

class TestFormTestCase(unittest.TestCase):

    

    def test_load(self):
        form_class = LoginForm
        form_class.password = 'May'
        result =LoginForm.load(form_class)
        print(result)





