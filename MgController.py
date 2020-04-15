from pymongo import MongoClient
import pymongo
from Administrator import Administrator
from Member import Member


class MgController:

    def __init__(self):
        self.cluster = MongoClient(
            "mongodb+srv://wz:1999314Zwh%2F@attendancemanagementsystem-7immk.mongodb.net/test?retryWrites=true&w"
            "=majority")
        self.db = self.cluster["AMS"]
        self.admin_collection = self.db["Administrator"]
        self.member_collection = self.db["Member"]

    def download_data(self, administrator_list, member_list):
        self.download_admin(administrator_list)
        self.download_member(member_list)

    def download_admin(self, administrator_list):
        admins = self.admin_collection.find()
        if admins.count() != 0:
            for i in admins:
                admin = Administrator(i["name"], i["_id"], i["email_address"], i["password"])
                self.pend_members(admin, i["pending_members"])
                self.add_members(admin, i["added_members"])
                administrator_list.append(admin)

    def download_member(self, member_list):
        members = self.member_collection.find()
        if members.count() != 0:
            for i in self.member_collection.find():
                member = Member(i["name"], i["_id"], i["email_address"], i["password"])
                self.add_clubs(member, i["clubs"])
                member_list.append(member)

    def add_clubs(self, member, clubs):
        if clubs:
            for i in clubs:
                club_from_db = self.admin_collection.find_one({"_id": i})
                member.get_admin_list().append(
                    Administrator(club_from_db["name"], club_from_db["_id"], club_from_db["email_address"],
                                  club_from_db["password"]))

    def pend_members(self, admin, pending_members):
        if pending_members:
            for i in pending_members:
                member_from_db = self.member_collection.find_one({"_id": i})
                admin.pend_member(Member(member_from_db["name"], member_from_db["_id"], member_from_db["email_address"],
                                         member_from_db["password"]))

    def add_members(self, admin, added_members):
        if added_members:
            for i in added_members:
                member_from_db = self.member_collection.find_one({"_id": i})
                admin.add_member(Member(member_from_db["name"], member_from_db["_id"], member_from_db["email_address"],
                                        member_from_db["password"]))
