from django.test import TestCase

import unittest
from .models import *
# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='hal', password = 'prex123')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()



if __name__ == '__main__':
    unittest.main()