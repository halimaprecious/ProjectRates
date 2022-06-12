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

class TestProject(TestCase):

    def setUp(self):
        self.user = User.objects.create(id=1, username='cate')
        self.project = Projects.objects.create(id=1, title='test post', image='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='desc',owner=self.user, link='http://ur.coml')


    def test_instance(self):
        self.assertTrue(isinstance(self.project, Projects))

    def test_save_project(self):
        self.project.save_project()
        post = Projects.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_projects(self):
        self.project.save()
        posts = Projects.get_projects()
        self.assertTrue(len(posts) > 0)

    def test_search_project(self):
        self.project.save()
        post = Projects.search_projects('test')
        self.assertTrue(len(post) > 0)

    def test_delete_project(self):
        self.project.delete_project()
        post = Projects.search_projects('test')
        self.assertTrue(len(post) < 1)

if __name__ == '__main__':
    unittest.main()