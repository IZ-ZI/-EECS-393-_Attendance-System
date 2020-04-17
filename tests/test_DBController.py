import unittest
from datetime import datetime

import mongomock
from DBController import DBController
from Member import Member
from Administrator import Administrator
from Activity import Activity


class test_DBController(unittest.TestCase):
    # def setUp(self):
    #     self.collection = mongomock.MongoClient().db.collection
    #     m1 = Member("name_test", "id_111", "email", "password")
    #     post1 = {"_id": "123", "name": "graves", "date": "apr.9"}
    #     self.collection.insert_one(post1)

    def setUp(self):
        self.database = mongomock.MongoClient().db
        post1 = {"_id": "393", "name": "software", "email_address": "eecs393@gmail.com", "password": "pass"}

        self.collection_admin = self.database.create_collection("Administrator")
        self.collection_admin.insert_one(post1)

        post2 = {"_id": "123", "name": "Terry", "email_address": "terry@gmail.com", "password": "pass"}
        self.collection_member = self.database.create_collection("Member")
        self.collection_member.insert_one(post2)

        post3 = {"_id": "888", "name": "meeting", "start_time": "Apr10", "end_time": "Apr11", "location": "case"}

        self.collection_activity = self.database.create_collection("Activity")
        self.collection_activity.insert_one(post3)

        self.db = DBController(self.collection_member, self.collection_admin, self.collection_activity)

    def test_member_is_present(self):
        self.assertTrue(self.db.member_is_present("123"))
        self.assertFalse(self.db.member_is_present("000"))

    def test_add_member(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        # member1 is not in the collection
        self.assertTrue(self.db.add_member(member1))
        # member1 already exists
        self.assertFalse(self.db.add_member(member1))
        # member2 already exists when construct
        member2 = Member("Terry", "123", "terry@gmail.com", "pass")
        self.assertFalse(self.db.add_member(member2))

    def test_update_member(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.assertFalse(self.db.update_member(member1))
        member2 = Member("Terry", "123", "terry@gmail.com", "change_password")
        self.assertTrue(self.db.update_member(member2))

    def test_retrieve_member(self):
        self.assertEqual(self.collection_member.find_one({"_id": "123"}), self.db.retrieve_member("123"))
        self.assertIsNone(self.db.retrieve_member("000"))

    def test_retrieve_member_name(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_member(member1)
        self.assertEqual(self.db.retrieve_member_name("123"), "Terry")
        self.assertEqual(self.db.retrieve_member_name("847"), "Marcus")

    def test_delete_member(self):
        self.assertTrue(self.db.delete_member("123"))
        self.assertFalse(self.db.delete_member("123"))

    def test_member_login(self):
        self.assertTrue(self.db.member_login("123", "pass"))
        self.assertFalse(self.db.member_login("00", "pass"))
        self.assertFalse(self.db.member_login("123", "wrong_password"))

    def test_clubs_member_added(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_member(member1)
        # self.assertIsNotNone(self.db.clubs_member_added("123"))
        self.assertIsNotNone(self.db.clubs_member_added("847"))
        self.assertIsNone(self.db.clubs_member_added("000"))

    def test_add_club_to_member(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_member(member1)
        self.assertTrue(self.db.add_club_to_member("393", "847"))
        self.assertFalse(self.db.add_club_to_member("393", "847"))
        self.assertFalse(self.db.add_club_to_member("000", "847"))

    def test_remove_club_from_member(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_member(member1)
        self.db.add_club_to_member("393", "847")
        self.assertTrue(self.db.remove_club_from_member("393", "847"))
        self.assertFalse(self.db.remove_club_from_member("000", "847"))

    def test_request_permission(self):
        admin1 = Administrator("terry", "110", "terry@gmail.com", "pass")
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.assertTrue(self.db.request_permission("110", "847", "terry@gmail.com", "Marcus"))
        self.assertFalse(self.db.request_permission("000", "847", "terry@gmail.com", "Marcus"))
        self.assertFalse(self.db.request_permission("110", "847", "terry@gmail.com", "Marcus"))

    def test_admin_is_present(self):
        self.assertTrue(self.db.admin_is_present("393"))
        self.assertFalse(self.db.admin_is_present("000"))

    def test_update_member_face_id(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_member(member1)
        self.assertTrue(self.db.update_member_face_id("847", "face_id"))
        self.assertFalse(self.db.update_member_face_id("000", "face_id"))

    def test_retrieve_member_face_id(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_member(member1)
        self.db.update_member_face_id("847", "face_id")
        self.assertEqual(self.db.retrieve_member_face_id("847"), "face_id")

    def test_add_admin(self):
        admin1 = Administrator("new_admin", "000", "new@gmail.com", "new_password")
        self.assertTrue(self.db.add_admin(admin1))
        self.assertFalse(self.db.add_admin(admin1))

    def test_update_admin(self):
        admin1 = Administrator("software", "393", "new@gmail.com", "new_password")
        self.assertTrue(self.db.update_admin(admin1))
        admin2 = Administrator("new_admin", "000", "new@gmail.com", "new_password")
        self.assertFalse((self.db.update_admin(admin2)))

    def test_retrieve_admin(self):
        self.assertEqual(self.db.retrieve_admin("393"), self.collection_admin.find_one({"_id": "393"}))
        self.assertIsNone(self.db.retrieve_admin("000"))

    def test_delete_admin(self):
        self.assertTrue(self.db.delete_admin("393"))
        self.assertFalse(self.db.delete_admin("000"))

    def test_admin_login(self):
        self.assertTrue(self.db.admin_login("393", "pass"))
        self.assertFalse(self.db.admin_login("393", "wrong_pass"))
        self.assertFalse(self.db.admin_login("000", "pass"))

    def test_add_member_to_added_members(self):
        admin1 = Administrator("terry", "110", "terry@gmail.com", "pass")
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.assertTrue(self.db.add_member_to_added_members("110", "847"))
        self.assertFalse(self.db.add_member_to_added_members("110", "847"))
        self.assertFalse(self.db.add_member_to_added_members("000", "847"))

    def test_remove_member_from_added_members(self):
        admin1 = Administrator("terry", "110", "terry@gmail.com", "pass")
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.db.add_member_to_added_members("110", "847")
        self.assertFalse(self.db.remove_member_from_added_members("000", "847"))
        self.assertFalse(self.db.remove_member_from_added_members("110", "000"))
        self.assertTrue(self.db.remove_member_from_added_members("110", "847"))

    def test_add_member_to_pending_members(self):
        admin1 = Administrator("terry", "110", "terry@gmail.com", "pass")
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.assertTrue(self.db.add_member_to_pending_members("110", "847"))
        self.assertFalse(self.db.add_member_to_pending_members("000", "847"))

    def test_remove_member_from_pending_members(self):
        admin1 = Administrator("terry", "110", "terry@gmail.com", "pass")
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.db.add_member_to_pending_members("110", "847")
        self.assertFalse(self.db.remove_member_from_pending_members("000", "847"))
        self.assertFalse(self.db.remove_member_from_pending_members("110", "000"))
        self.assertTrue(self.db.remove_member_from_pending_members("110", "847"))

    def test_added_members(self):
        admin1 = Administrator("terry", "110", "terry@gmail.com", "pass")
        self.db.add_admin(admin1)
        self.assertIsNotNone(self.db.added_members("110"))
        self.assertEqual([], self.db.added_members("110"))

    def test_pending_members(self):
        admin1 = Administrator("terry", "110", "terry@gmail.com", "pass")
        self.db.add_admin(admin1)
        self.assertIsNotNone(self.db.pending_members("110"))
        self.assertEqual([], self.db.pending_members("110"))

    def test_permit(self):
        admin1 = Administrator("terry", "110", "terry@gmail.com", "pass")
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.db.add_member_to_pending_members("110", "847")
        self.assertTrue(self.db.permit("xxl844@gmail.com", "110", "terry"))

    def test_reject(self):
        admin1 = Administrator("terry", "110", "terry@gmail.com", "pass")
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.db.add_member_to_pending_members("110", "847")
        self.assertTrue(self.db.reject("xxl844@gmail.com", "110", "terry"))

    def test_activity_is_present(self):
        self.assertTrue(self.db.activity_is_present("888"))
        self.assertFalse(self.db.activity_is_present("000"))

    def test_add_activity(self):
        activity1 = Activity("999", "party", datetime(2020, 2, 2, 3, 20), datetime(2020, 2, 2, 4, 30), "case")
        self.assertTrue(self.db.add_activity(activity1, "393"))
        self.assertFalse(self.db.add_activity(activity1, "393"))

    def test_update_activity(self):
        activity1 = Activity("888", "party", datetime(2020, 2, 2, 3, 20), datetime(2020, 2, 2, 4, 30), "case")
        activity2 = Activity("000", "party", datetime(2020, 2, 2, 3, 20), datetime(2020, 2, 2, 4, 30), "case")
        self.assertTrue(self.db.update_activity(activity1))
        self.assertFalse(self.db.update_activity(activity2))

    def test_retrieve_activity(self):
        self.assertEqual(self.collection_activity.find_one({"_id": "888"}), self.db.retrieve_activity("888"))
        self.assertIsNone(self.db.retrieve_activity("000"))

    def test_delete_activity(self):
        self.assertTrue(self.db.delete_activity("888"))
        self.assertFalse(self.db.delete_activity("000"))

    def test_add_activity_to_member(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_member(member1)
        self.assertTrue(self.db.add_activity_to_member("393", "888", "847", "on_time"))
        self.assertFalse(self.db.add_activity_to_member("393", "888", "847", "on_time"))

    def test_set_member_activity_status(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_member(member1)
        self.db.add_activity_to_member("393", "888", "847", "on_time")
        self.assertTrue(self.db.set_member_activity_status("393", "888", "847", "on_time"))
        self.assertFalse(self.db.set_member_activity_status("393", "000", "847", "on_time"))

    def test_remove_activity_from_member(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_member(member1)
        self.db.add_activity_to_member("393", "888", "847", "on_time")
        self.assertTrue(self.db.remove_activity_from_member("393", "888", "847"))
        self.assertFalse(self.db.remove_activity_from_member("393", "888", "847"))

    def test_add_activity_to_admin(self):
        admin1 = Administrator("terry", "110", "terry@gmail.com", "pass")
        self.db.add_admin(admin1)
        self.assertTrue(self.db.add_activity_to_admin("888", "110"))
        self.assertFalse(self.db.add_activity_to_admin("888", "000"))

    def test_remove_activity_from_admin(self):
        admin1 = Administrator("terry", "110", "terry@gmail.com", "pass")
        self.db.add_admin(admin1)
        self.db.add_activity_to_admin("888", "110")
        self.assertTrue(self.db.remove_activity_from_admin("888", "110"))
        self.assertFalse(self.db.remove_activity_from_admin("888", "110"))

    def test_member_status_in_activity(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_member(member1)
        self.db.add_activity_to_member("393", "888", "847", "on_time")
        self.db.set_member_activity_status("393", "888", "847", "on_time")
        self.assertEqual(self.db.member_status_in_activity("847", "393", "888"), "on_time")

    def test_member_activities(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_member(member1)
        self.assertEqual(self.db.member_activities("847"), [])
        self.assertIsNone(self.db.member_activities("000"))

    def test_admin_activities(self):
        admin1 = Administrator("new_admin", "000", "new@gmail.com", "new_password")
        self.db.add_admin(admin1)
        self.assertEqual(self.db.admin_activities("000"), [])
        self.assertIsNone(self.db.admin_activities("111"))

    def test_activity_start_time(self):
        self.assertEqual(self.db.activity_start_time("888"), "Apr10")
        self.assertIsNone(self.db.activity_start_time("000"))

    def test_activity_end_time(self):
        self.assertEqual(self.db.activity_end_time("888"), "Apr11")
        self.assertIsNone(self.db.activity_end_time("000"))

    # def test_self_insert(self):
    #     results = self.collection_member.find_one({"_id": "123"})
    #     a = results["_id"]
    #     self.assertEqual(a, "123")
    #
    def test_retrieve_member_name(self):
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_member(member1)
        self.assertEqual(self.db.retrieve_member_name("123"), "Terry")
        self.assertEqual(self.db.retrieve_member_name("847"), "Marcus")

        def test_member_status_in_activity(self):
            member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
            self.db.add_member(member1)
            self.db.add_activity_to_member("393", "888", "847", "on_time")
            self.db.set_member_activity_status("393", "888", "847", "on_time")
            self.assertEqual(self.db.member_status_in_activity("847", "393", "888"), "on_time")