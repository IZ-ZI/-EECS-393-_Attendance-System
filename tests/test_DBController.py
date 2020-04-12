import unittest
import mongomock
from DBController_for_test import DBController_for_test
from Member import Member
from Administrator import Administrator

class test_DBController(unittest.TestCase):
    # def setUp(self):
    #     self.collection = mongomock.MongoClient().db.collection
    #     m1 = Member("name_test", "id_111", "email", "password")
    #     post1 = {"_id": "123", "name": "graves", "date": "apr.9"}
    #     self.collection.insert_one(post1)

    def setUp(self):
        self.database = mongomock.MongoClient().db
        post1 = {"_id": "393", "name": "software",
                "email_address": "eecs393@gmail.com",
                "password": "pass"}
        # "added_members": [], "pending_members": []

        self.collection_admin = self.database.create_collection("Administrator")
        self.collection_admin.insert_one(post1)

        post2 = {"_id": "123", "name": "Terry", "email_address": "terry@gmail.com","password":"pass"}
        self.collection_member = self.database.create_collection("Member")
        self.collection_member.insert_one(post2)
        self.db = DBController_for_test(self.collection_member, self.collection_admin)

    def test_member_is_present(self):
        self.assertTrue(self.db.member_is_present("123"))
        self.assertFalse(self.db.member_is_present("000"))

    def test_add_member(self):
        member1 = Member("Marcus","847","xxl844@gmail.com","password")
        # member1 is not in the collection
        self.assertTrue(self.db.add_member(member1))
        # member1 already exists
        self.assertFalse(self.db.add_member(member1))
        # member2 already exists when construct
        member2 = Member("Terry","123","terry@gmail.com","pass")
        self.assertFalse(self.db.add_member(member2))

    def test_update_member(self):
        member1 = Member("Marcus","847","xxl844@gmail.com","password")
        self.assertFalse(self.db.update_member(member1))
        member2 = Member("Terry", "123", "terry@gmail.com", "change_password")
        self.assertTrue(self.db.update_member(member2))

    def test_retrieve_member(self):
        self.assertEqual(self.collection_member.find_one({"_id": "123"}), self.db.retrieve_member("123"))
        self.assertIsNone(self.db.retrieve_member("000"))

    def test_delete_member(self):
        self.assertTrue(self.db.delete_member("123"))
        self.assertFalse(self.db.delete_member("123"))

    def test_member_login(self):
        self.assertTrue(self.db.member_login("123","pass"))
        self.assertFalse(self.db.member_login("00","pass"))
        self.assertFalse(self.db.member_login("123","wrong_password"))

    def test_clubs_member_added(self):
        member1 = Member("Marcus","847","xxl844@gmail.com","password")
        self.db.add_member(member1)
        # self.assertIsNotNone(self.db.clubs_member_added("123"))
        self.assertIsNotNone(self.db.clubs_member_added("847"))
        self.assertIsNone(self.db.clubs_member_added("000"))

    def test_add_club_to_member(self):
        member1 = Member("Marcus","847","xxl844@gmail.com","password")
        self.db.add_member(member1)
        self.assertTrue(self.db.add_club_to_member("393","847"))
        self.assertFalse(self.db.add_club_to_member("393","847"))
        self.assertFalse(self.db.add_club_to_member("000","847"))

    def test_remove_club_from_member(self):
        member1 = Member("Marcus","847","xxl844@gmail.com","password")
        self.db.add_member(member1)
        self.db.add_club_to_member("393", "847")
        self.assertTrue(self.db.remove_club_from_member("393","847"))
        self.assertFalse(self.db.remove_club_from_member("000","847"))

    def test_request_permission(self):
        admin1 = Administrator("terry", "110", "terry@gmail.com", "pass")
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.assertTrue(self.db.request_permission("110", "847", "terry@gmail.com", "Marcus"))

    def test_admin_is_present(self):
        self.assertTrue(self.db.admin_is_present("393"))
        self.assertFalse(self.db.admin_is_present("000"))

    def test_add_admin(self):
        admin1 = Administrator("new_admin","000","new@gmail.com","new_password")
        self.assertTrue(self.db.add_admin(admin1))
        self.assertFalse(self.db.add_admin(admin1))

    def test_update_admin(self):
        admin1 = Administrator("software","393","new@gmail.com","new_password")
        self.assertTrue(self.db.update_admin(admin1))
        admin2 = Administrator("new_admin","000","new@gmail.com","new_password")
        self.assertFalse((self.db.update_admin(admin2)))

    def test_retrieve_admin(self):
        self.assertEqual(self.db.retrieve_admin("393"),self.collection_admin.find_one({"_id":"393"}))
        self.assertIsNone(self.db.retrieve_admin("000"))

    def test_delete_admin(self):
        self.assertTrue(self.db.delete_admin("393"))
        self.assertFalse(self.db.delete_admin("000"))

    def test_admin_login(self):
        self.assertTrue(self.db.admin_login("393","pass"))
        self.assertFalse(self.db.admin_login("393","wrong_pass"))
        self.assertFalse(self.db.admin_login("000","pass"))

    def test_add_member_to_added_members(self):
        admin1 = Administrator("terry","110","terry@gmail.com","pass")
        member1 = Member("Marcus","847","xxl844@gmail.com","password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.assertTrue(self.db.add_member_to_added_members("110","847"))
        self.assertFalse(self.db.add_member_to_added_members("110","847"))
        self.assertFalse(self.db.add_member_to_added_members("000","847"))

    def test_remove_member_from_added_members(self):
        admin1 = Administrator("terry","110","terry@gmail.com","pass")
        member1 = Member("Marcus","847","xxl844@gmail.com","password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.db.add_member_to_added_members("110", "847")
        self.assertFalse(self.db.remove_member_from_added_members("000", "847"))
        self.assertFalse(self.db.remove_member_from_added_members("110", "000"))
        self.assertTrue(self.db.remove_member_from_added_members("110", "847"))

    def test_add_member_to_pending_members(self):
        admin1 = Administrator("terry","110","terry@gmail.com","pass")
        member1 = Member("Marcus","847","xxl844@gmail.com","password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.assertTrue(self.db.add_member_to_pending_members("110", "847"))
        self.assertFalse(self.db.add_member_to_pending_members("000", "847"))

    def test_remove_member_from_pending_members(self):
        admin1 = Administrator("terry","110","terry@gmail.com","pass")
        member1 = Member("Marcus","847","xxl844@gmail.com","password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.db.add_member_to_pending_members("110", "847")
        self.assertFalse(self.db.remove_member_from_pending_members("000", "847"))
        self.assertFalse(self.db.remove_member_from_pending_members("110", "000"))
        self.assertTrue(self.db.remove_member_from_pending_members("110", "847"))

    def test_added_members(self):
        admin1 = Administrator("terry","110","terry@gmail.com","pass")
        self.db.add_admin(admin1)
        self.assertIsNotNone(self.db.added_members("110"))
        self.assertEqual([],self.db.added_members("110"))

    def test_pending_members(self):
        admin1 = Administrator("terry","110","terry@gmail.com","pass")
        self.db.add_admin(admin1)
        self.assertIsNotNone(self.db.pending_members("110"))
        self.assertEqual([],self.db.pending_members("110"))

    def test_permit(self):
        admin1 = Administrator("terry","110", "terry@gmail.com","pass")
        member1 = Member("Marcus","847","xxl844@gmail.com","password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.db.add_member_to_pending_members("110", "847")
        self.assertTrue(self.db.permit("847", "xxl844@gmail.com", "110", "terry@gmail.com"))

    def test_reject(self):
        admin1 = Administrator("terry", "110", "terry@gmail.com", "pass")
        member1 = Member("Marcus", "847", "xxl844@gmail.com", "password")
        self.db.add_admin(admin1)
        self.db.add_member(member1)
        self.db.add_member_to_pending_members("110", "847")
        self.assertTrue(self.db.reject("847", "xxl844@gmail.com", "110", "terry@gmail.com"))

    # def test_self_insert(self):
    #     results = self.collection_member.find_one({"_id": "123"})
    #     a = results["_id"]
    #     self.assertEqual(a, "123")
    #