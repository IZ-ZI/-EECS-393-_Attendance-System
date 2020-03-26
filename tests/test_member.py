import unittest
from mock import Mock

from Member import Member
from WaitList import WaitList


def constructorMock(name):
    """Create fake constructor that returns Mock object when invoked"""
    instance = Mock()
    instance._name_of_parent_class = name
    constructor = Mock(return_value=instance)
    return constructor


class MemberTestCase(unittest.TestCase):
    wl = None
    mber = None

    def setUp(self):
        global wl, mber
        wl = WaitList()
        mber = Member('Test Subject', '12345', 'testsubject@email.com', 'foo', wl)
        Member.WaitList = constructorMock("WaitList")

    def test_create_member(self):
        """create a member instance and check its properties"""
        global wl, mber
        wait_list = Member.WaitList.return_value
        self.assertEqual(wait_list._name_of_parent_class, 'WaitList')
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

    def test_attendanceRecord(self):
        global mber
        attendance_data = mber.attendanceRecord()
        self.assertIsInstance(attendance_data, list)


if __name__ == '__main__':
    unittest.main()
