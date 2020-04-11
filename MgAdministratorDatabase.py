from pymongo import MongoClient
import pymongo


class MgAdministratorDatabase:

    def __init__(self):
        self.cluster = MongoClient(
            "mongodb+srv://wz:1999314Zwh%2F@attendancemanagementsystem-7immk.mongodb.net/test?retryWrites=true&w"
            "=majority")
        self.db = self.cluster["AMS"]
        self.collection = self.db["Administrator"]

    def is_present(self, admin_id):
        admin = self.collection.find_one({"_id": admin_id})
        return admin is not None

    def add(self, admin):
        if not self.is_present(admin.get_organization_id()):
            post = {"_id": admin.get_organization_id(), "name": admin.get_organization_name(),
                    "email_address": admin.get_email_address(),
                    "password": admin.get_password(), "added_members": [], "pending_members": []}
            self.collection.insert_one(post)
            return True
        else:
            return False

    def update(self, admin):
        if self.is_present(admin.get_organization_id()):
            self.collection.update_one({"_id": admin.get_organization_id()}, {'$set':
                {
                    "name": admin.get_organization_name(), "email_address": admin.get_email_address(),
                    "password": admin.get_password()
                }
            })
            return True
        else:
            return False

    # return a dictionary in a form like "_id": admin.get_organization_id(), "name": admin.get_organization_name(),
    # "email_address": admin.get_email_address(),"password": admin.get_password(), "clubs": []
    def retrieve(self, admin_id):
        return self.collection.find_one({"_id": admin_id})

    def delete(self, admin_id):
        if self.is_present(admin_id):
            self.collection.delete_one({"_id": admin_id})
            return True
        else:
            return False

    def login(self, admin_id, password):
        if not self.is_present(admin_id):
            return None

        admin = self.retrieve(admin_id)
        if admin["password"] == password:
            return admin
        else:
            return None

    def add_member_to_added_members(self, admin_id, member_id):
        if self.is_present(admin_id):
            self.collection.update_one(
                {"_id": admin_id},
                {'$push': {"added_members": member_id}}
            )
            return True
        else:
            return False

    def remove_member_from_added_members(self, admin_id, member_id):
        if self.is_present(admin_id):
            self.collection.update_one(
                {"_id": admin_id},
                {'$pull': {"added_members": member_id}}
            )
            return True
        else:
            return False

    def add_member_to_pending_members(self, admin_id, member_id):
        if self.is_present(admin_id):
            self.collection.update_one(
                {"_id": admin_id},
                {'$push': {"pending_members": member_id}}
            )
            return True
        else:
            return False

    def remove_member_from_pending_members(self, admin_id, member_id):
        if self.is_present(admin_id):
            self.collection.update_one(
                {"_id": admin_id},
                {'$pull': {"pending_members": member_id}}
            )
            return True
        else:
            return False

    def added_members(self, admin_id):
        if self.is_present(admin_id):
            cursor = self.collection.find_one({"_id": admin_id})
            return cursor["added_members"]
        else:
            return None

    def pending_members(self, admin_id):
        if self.is_present(admin_id):
            cursor = self.collection.find_one({"_id": admin_id})
            return cursor["pending_members"]
        else:
            return None
