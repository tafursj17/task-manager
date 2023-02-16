from django.test import TestCase
from ..models import User
from model_mommy import mommy

# Create your tests here.
class TestNote(TestCase):

    def setUp(self) -> None:
        self.username_1 = 'Andres12'
        self.username_2 = 'Sebastian'
        self.username_3 = 'JuanitaP'

    def test_create_object_user(self):
        u1 = User.objects.create(username= self.username_1)
        self.assertIsNotNone(u1)
        self.assertEqual(u1.__str__(), self.username_1)
    
    def test_create_object_user(self):
        u1 = User.objects.create(username= self.username_1)
        self.assertIsNotNone(u1)
        self.assertEqual(u1.__str__(), self.username_1)

    def test_create_object_user(self):
        u1 = User.objects.create(username= self.username_1)
        self.assertIsNotNone(u1)
        self.assertEqual(u1.__str__(), self.username_1)