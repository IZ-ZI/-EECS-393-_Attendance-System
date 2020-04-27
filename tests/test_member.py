import unittest
from mock import Mock

from Member import Member

import sys
sys.path.insert(0, 'D:\EECS393Project\-EECS-393-_Attendance-System')

class MemberTestCase(unittest.TestCase):
    mber = None

    def setUp(self):
        global mber
        mber = Member('Test Subject', '12345', 'testsubject@email.com', 'foo')

    def test_create_member(self):
        """create a member instance and check its properties"""
        global mber
        self.assertEqual(isinstance(mber, Member), True)

    def test_get_name(self):
        global mber
        name = mber.get_name()
        self.assertEqual(name, 'Test Subject')

    def test_get_id(self):
        global mber
        id = mber.get_id()
        self.assertEqual(id, '12345')

    def test_get_email_address(self):
        global mber
        email = mber.get_email_address()
        self.assertEqual(email, 'testsubject@email.com')

    def test_get_admin_list(self):
        global mber
        admins = mber.get_admin_list()
        self.assertIsInstance(admins, list)

    def test_get_average_score(self):
        global mber
        score = mber.averageScore()
        self.assertEqual(score, 0)

