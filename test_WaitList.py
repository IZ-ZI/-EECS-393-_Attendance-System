from unittest import TestCase
from Administrator import Administrator
from Member import Member
from WaitList import WaitList

class TestSetUp(TestCase):
    def setUp(self):
        self.w1 = WaitList()
        self.a1 = Administrator("1", "a", "www.1", "123", self.w1)
        self.m1 = Member("11", "z" , "www.11", "123", self.w1)

class TestWaitList(TestSetUp):

    def test_put_admin_in(self):
        self.w1.put_admin_in(self.a1)
        self.assertTrue(self.a1 in self.w1.get_list())

    def test_put_member_in(self):
        self.w1.put_admin_in(self.a1)
        self.w1.put_member_in(self.m1, self.a1)
        self.assertTrue(self.m1 in self.w1.get_list().get(self.a1))

    def test_pending_members(self):
        self.w1.put_admin_in(self.a1)
        self.w1.put_member_in(self.m1, self.a1)
        self.assertTrue(self.m1 in self.w1.pending_members(self.a1))

    def test_permit(self):
        self.w1.put_admin_in(self.a1)
        self.w1.put_member_in(self.m1, self.a1)
        self.assertEqual(self.w1.get_list().get(self.a1).get(self.m1), 0)
        self.w1.permit(self.m1, self.a1)
        self.assertEqual(self.w1.get_list().get(self.a1).get(self.m1), 1)

    def test_reject(self):
        self.w1.put_admin_in(self.a1)
        self.w1.put_member_in(self.m1, self.a1)
        self.assertEqual(self.w1.get_list().get(self.a1).get(self.m1), 0)
        self.w1.reject(self.m1, self.a1)
        self.assertEqual(self.w1.get_list().get(self.a1).get(self.m1), 2)


   # def test_delete(self):
   #     self.fail()

   # def test_is_member_in(self):
   #     self.fail()

   # def test_is_admin_in(self):
   #     self.fail()
