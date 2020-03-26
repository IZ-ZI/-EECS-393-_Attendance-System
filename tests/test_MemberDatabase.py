from unittest import TestCase
from MemberDatabase import MemberDatabase
from Member import Member

class TestMemberDatabase(TestCase):
    tester = MemberDatabase()
    mem1 = Member("A", "A_id", "a@email.com", "a")
    mem2 = Member("B", "B_id", "b@email.com", "b")

    def test_is_present(self):
        # test 0
       # self.assertFalse(self.tester.is_present("B_id"))

        # test 1
        self.tester.add(self.mem1)
        self.assertTrue(self.tester.is_present("A_id"))
        self.assertFalse(self.tester.is_present("B_id"))

        # test many
        self.tester.add(self.mem2)
        self.assertTrue(self.tester.is_present("A_id"))
        self.assertTrue(self.tester.is_present("B_id"))
        self.assertFalse(self.tester.is_present("???"))


    def test_add(self):
        self.assertTrue(self.tester.add(self.mem1))
        self.assertTrue(self.tester.add(self.mem2))
        self.assertFalse(self.tester.add(self.mem1))

'''
    def test_update(self):
        self.fail()

    def test_retrieve(self):
        self.fail()

    def test_delete(self):
        self.fail()

    def test_login(self):
        self.fail()

    def test_permit_pending_member(self):
        self.fail()

    def test_reject_pending_member(self):
        self.fail()
'''