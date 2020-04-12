import unittest
import mongomock
from DBController_for_test import DBController_for_test
from Member import Member


class test_DBController(unittest.TestCase):
    # def setUp(self):
    #     self.collection = mongomock.MongoClient().db.collection
    #     m1 = Member("name_test", "id_111", "email", "password")
    #     post1 = {"_id": "123", "name": "graves", "date": "apr.9"}
    #     self.collection.insert_one(post1)

    def setUp(self):
        self.database = mongomock.MongoClient().db
        self.collection_admin = self.database.create_collection("Administrator")
        post1 = {"_id": "123", "name": "Terry", "date": "apr9"}
        self.collection_member = self.database.create_collection("Member")
        self.collection_member.insert_one(post1)
        self.db = DBController_for_test(self.collection_member, self.collection_admin)

    def test_member_is_present(self):
        self.assertTrue(self.db.member_is_present("123"))
        self.assertFalse(self.db.member_is_present("000"))

    def test_add_member(self):
        member1 = Member("Marcus","847","xxl844@gmail.com","password")
        self.assertTrue(self.db.add_member(member1))
        self.assertFalse(self.db.add_member(member1))


        # objects = [
        #     {'group_field': 0, 'sum_field': 15},
        #     {'group_field': 1, 'sum_field': 30},
        #     {'group_field': 0, 'sum_field': 82},
        #     {'group_field': 2, 'sum_field': 3},
        #     {'group_field': 1, 'sum_field': 56},
        #     {'group_field': 3, 'sum_field': 15},
        #     {'group_field': 4, 'sum_field': 20},
        #     {'group_field': 1, 'sum_field': 30},
        #     {'group_field': 2, 'sum_field': 45},
        #     {'group_field': 4, 'sum_field': 82},
        #     {'group_field': 3, 'sum_field': 3},
        #     {'group_field': 2, 'sum_field': 56}
        # ]
        # for obj in objects:
        #     self.collection.insert_one(obj)

    def a(self):
        results = self.collection_member.find({"_id": "123"})
        print(results["_id"])

    def test_self_insert(self):
        results = self.collection_member.find_one({"_id": "123"})
        a = results["_id"]
        self.assertEqual(a, "123")


