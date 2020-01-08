from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from chat.models import Group, Message

# Create your tests here.


class AddUserGroup(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user('lucas', None, '123')
        self.user2 = User.objects.create_user('pepe', None, '123')
        self.group_python = Group.objects.create(name='python')

    def test_add_user_to_group(self):
        self.group_python.members.add(self.user1)
        self.group_python.members.add(self.user2)
        self.assertEquals(len(self.group_python.members.all()), 2)

    def test_create_message_of_group(self):
        self.message1 = Message.objects.create(
            content='Hello world', group=self.group_python, author=self.user1
        )

        self.message2 = Message.objects.create(
            content='Hello world again', group=self.group_python, author=self.user2
        )

        #print(str((self.group_python.message_of_group.all()).query)
        #print('#1: {}'.format(Message.objects.filter(group=self.group_python).count()))
        #print('cantidad: {}'.format(len(self.group_python.message_of_group.all())))
        self.assertEquals(len(self.group_python.message_of_group.all()), 2)


        