from unittest import TestCase
from Administrator import Administrator
from Member import Member



class TestAdministrator(TestCase):
    def setUp(self):
        self.a1 = Administrator("a", "1", "www.1", "123")
        self.m1 = Member("z", "111", "www.9", "321")

    def test_get_organization_id(self):
        self.assertEqual(self.a1.get_organization_id(), "1")
        self.assertFalse(self.a1.get_organization_id() == "2")

    def test_get_organization_name(self):
        self.assertEqual(self.a1.get_organization_name(), "a")
        self.assertFalse(self.a1.get_organization_name() == "b")

    def test_get_email_address(self):
        self.assertEqual(self.a1.get_email_address(), "www.1")
        self.assertFalse(self.a1.get_email_address() == "www.2")

    def test_get_password(self):
        self.assertEqual(self.a1.get_password(), "123")
        self.assertFalse(self.a1.get_password() == "321")
