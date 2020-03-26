from unittest import TestCase
from MemberDatabase import MemberDatabase
from Member import Member

class TestMemberDatabase(TestCase):
    tester = MemberDatabase()
    mem1 = Member("A", "A_id", "a@email.com", "a")
    mem2 = Member("B", "B_id", "b@email.com", "b")

    def test_is_present(self):
        self.tester.add(self.mem1)
        self.assertTrue(self.tester.is_present("A_id"))
        self.assertFalse(self.tester.is_present("B_id"))

    def test_add(self):
        self.tester.add(self.mem1)
        self.assertTrue(self.tester.is_present("A_id"))
        print(self.tester.add(self.mem1))
        print(self.tester.add(self.mem1))
        print(self.tester.add(self.mem1))
        print(self.tester.database)

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