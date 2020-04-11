from pymongo import MongoClient
import pymongo


class MgMemberDatabase:

    def __init__(self):
        self.cluster = MongoClient(
            "mongodb+srv://wz:1999314Zwh%2F@attendancemanagementsystem-7immk.mongodb.net/test?retryWrites=true&w"
            "=majority")
        self.db = self.cluster["AMS"]
        self.collection = self.db["Member"]

    def is_present(self, member_id):
        member = self.collection.find_one({"_id": member_id})
        return member is not None

    def add(self, member):
        if not self.is_present(member.get_id()):
            post = {"_id": member.get_id(), "name": member.get_name(), "email_address": member.get_email_address(),
                    "password": member.get_password(), "clubs": []}
            self.collection.insert_one(post)
            return True
        else:
            return False

    def update(self, member):
        if self.is_present(member.get_id()):
            self.collection.update_one({"_id": member.get_id()}, {'$set':
                {
                    "name": member.get_name(), "email_address": member.get_email_address(),
                    "password": member.get_password()
                }
            })
            return True
        else:
            return False

    # return a dictionary in a form like "_id": member.get_id(), "name": member.get_name(), "email_address":
    # member.get_email_address(),"password": member.get_password(), "clubs": []
    def retrieve(self, member_id):
        return self.collection.find_one({"_id": member_id})

    def delete(self, member_id):
        if self.is_present(member_id):
            self.collection.delete_one({"_id": member_id})
            return True
        else:
            return False

    def login(self, member_id, password):
        if not self.is_present(member_id):
            return None

        member = self.retrieve(member_id)
        if member["password"] == password:
            return member
        else:
            return None

    def add_club_to_member(self, club_id, member_id):
        if self.is_present(member_id):
            self.collection.update_one(
                {"_id": member_id},
                {'$push': {"clubs": club_id}}
            )
            return True
        else:
            return False

    def remove_club_from_member(self, club_id, member_id):
        if self.is_present(member_id):
            self.collection.update_one(
                {"_id": member_id},
                {'$pull': {"clubs": club_id}}
            )
            return True
        else:
            return False

    def clubs_member_added(self, member_id):
        if self.is_present(member_id):
            cursor = self.collection.find_one({"_id": member_id})
            return cursor["clubs"]
        else:
            return None