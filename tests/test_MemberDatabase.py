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
        self.assertFalse(self.tester.is_present("id"))
        self.tester.add(self.mem2)
        self.assertTrue(self.tester.is_present("A_id"))
        self.assertTrue(self.tester.is_present("B_id"))
        self.assertFalse(self.tester.is_present("???"))

    def test_add(self):
        self.assertTrue(self.tester.add(self.mem1))
        self.assertTrue(self.tester.add(self.mem2))
        self.assertFalse(self.tester.add(self.mem1))

    def test_update(self):
        self.tester.add(self.mem1)
        self.assertTrue(self.tester.retrieve("A_id").get_name() == "A")
        new_mem1 = Member("ABC", "A_id", "a@email.com", "a")
        self.tester.update(new_mem1)
        self.assertTrue(self.tester.retrieve("A_id").get_name() == "ABC")

    def test_retrieve(self):
        self.assertTrue(self.tester.retrieve("any") is None)
        self.tester.add(self.mem1)
        self.assertTrue(self.tester.retrieve("A_id") is self.mem1)
        self.tester.add(self.mem2)
        self.assertTrue(self.tester.retrieve("B_id") is self.mem2)

    def test_delete(self):
        self.assertFalse(self.tester.delete("any"))
        self.tester.add(self.mem1)
        self.assertTrue(self.tester.delete("A_id"))
        self.assertFalse(self.tester.is_present("A_id"))

        self.tester.add(self.mem1)
        self.tester.add(self.mem2)
        self.assertTrue(self.tester.delete("A_id"))
        self.assertTrue(self.tester.delete("B_id"))

        self.assertFalse(self.tester.is_present("A_id"))
        self.assertFalse(self.tester.is_present("A_id"))

    def test_login(self):
        self.assertTrue(self.tester.login("any", "any") is None)
        self.tester.add(self.mem1)
        self.assertTrue(self.tester.login("A_id", "a") is self.mem1)
        self.assertFalse(self.tester.login("A_id", "any") is self.mem1)
        self.tester.add(self.mem2)
        self.assertTrue(self.tester.login("B_id", "b") is self.mem2)
        self.assertFalse(self.tester.login("B_id", "any") is self.mem2)

    def test_permit_pending_member(self):
        self.assertTrue(self.tester.permit_pending_member("any") is None)
        self.tester.wait_list.append(self.mem1)
        self.assertTrue(self.tester.permit_pending_member("A_id") is self.mem1)
        self.assertTrue(len(self.tester.wait_list) == 0)
        self.assertTrue(self.tester.is_present("A_id"))

    def test_reject_pending_member(self):
        self.fail()
