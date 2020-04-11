from pymongo import MongoClient
import pymongo
import sendEmail as se


class DBController:

    def __init__(self):
        self.cluster = MongoClient(
            "mongodb+srv://wz:1999314Zwh%2F@attendancemanagementsystem-7immk.mongodb.net/test?retryWrites=true&w"
            "=majority")
        self.db = self.cluster["AMS"]
        self.collection_member = self.db["Member"]
        self.collection_admin = self.db["Administrator"]

    def member_is_present(self, member_id):
        member = self.collection_member.find_one({"_id": member_id})
        return member is not None

    def add_member(self, member):
        if not self.member_is_present(member.get_id()):
            post = {"_id": member.get_id(), "name": member.get_name(), "email_address": member.get_email_address(),
                    "password": member.get_password(), "clubs": []}
            self.collection_member.insert_one(post)
            return True
        else:
            return False

    def update_member(self, member):
        if self.member_is_present(member.get_id()):
            self.collection_member.update_one({"_id": member.get_id()}, {'$set':
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
    def retrieve_member(self, member_id):
        return self.collection_member.find_one({"_id": member_id})

    def delete_member(self, member_id):
        if self.member_is_present(member_id):
            self.collection_member.delete_one({"_id": member_id})
            return True
        else:
            return False

    def member_login(self, member_id, password):
        if not self.member_is_present(member_id):
            return False

        member = self.retrieve(member_id)
        if member["password"] == password:
            return True
        else:
            return False

    def clubs_member_added(self, member_id):
        if self.member_is_present(member_id):
            cursor = self.collection_member.find_one({"_id": member_id})
            return cursor["clubs"]
        else:
            return None

    def add_club_to_member(self, club_id, member_id):
        if self.admin_is_present(club_id) and club_id not in self.clubs_member_added(member_id):
            self.collection_member.update_one(
                {"_id": member_id},
                {'$push': {"clubs": club_id}}
            )
            return True
        else:
            return False

    def remove_club_from_member(self, club_id, member_id):
        if self.member_is_present(member_id) and club_id in self.clubs_member_added(member_id):
            self.collection_member.update_one(
                {"_id": member_id},
                {'$pull': {"clubs": club_id}}
            )
            return True
        else:
            return False

    def request_permission(self, admin_id, member_id, admin_email, member_name):
        if self.admin_is_present(admin_id) and member_id not in self.pending_members(admin_id):
            self.add_member_to_pending_members(admin_id, member_id)
            se.send_email('attsystem393@gmail.com', 'eecs_393', admin_email, member_name, member_id, True)
            return True
        else:
            return False
















    def admin_is_present(self, admin_id):
        admin = self.collection_admin.find_one({"_id": admin_id})
        return admin is not None

    def add_admin(self, admin):
        if not self.admin_is_present(admin.get_organization_id()):
            post = {"_id": admin.get_organization_id(), "name": admin.get_organization_name(),
                    "email_address": admin.get_email_address(),
                    "password": admin.get_password(), "added_members": [], "pending_members": []}
            self.collection_admin.insert_one(post)
            return True
        else:
            return False

    def update_admin(self, admin):
        if self.admin_is_present(admin.get_organization_id()):
            self.collection_admin.update_one({"_id": admin.get_organization_id()}, {'$set':
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
    def retrieve_admin(self, admin_id):
        return self.collection_admin.find_one({"_id": admin_id})

    def delete_admin(self, admin_id):
        if self.admin_is_present(admin_id):
            self.collection_admin.delete_one({"_id": admin_id})
            return True
        else:
            return False

    def admin_login(self, admin_id, password):
        if not self.admin_is_present(admin_id):
            return False

        admin = self.admin_retrieve(admin_id)
        if admin["password"] == password:
            return True
        else:
            return False

    def add_member_to_added_members(self, admin_id, member_id):
        if self.admin_is_present(admin_id) and member_id not in self.added_members(admin_id):
            self.collection_admin.update_one(
                {"_id": admin_id},
                {'$push': {"added_members": member_id}}
            )
            return True
        else:
            return False

    def remove_member_from_added_members(self, admin_id, member_id):
        if self.admin_is_present(admin_id) and member_id in self.added_members(admin_id):
            self.collection_admin.update_one(
                {"_id": admin_id},
                {'$pull': {"added_members": member_id}}
            )
            return True
        else:
            return False

    def add_member_to_pending_members(self, admin_id, member_id):
        if self.admin_is_present(admin_id) and member_id not in self.pending_members(admin_id):
            self.collection_admin.update_one(
                {"_id": admin_id},
                {'$push': {"pending_members": member_id}}
            )
            return True
        else:
            return False

    def remove_member_from_pending_members(self, admin_id, member_id):
        if self.admin_is_present(admin_id) and member_id in self.pending_members(admin_id):
            self.collection_admin.update_one(
                {"_id": admin_id},
                {'$pull': {"pending_members": member_id}}
            )
            return True
        else:
            return False

    def added_members(self, admin_id):
        cursor = self.collection_admin.find_one({"_id": admin_id})
        return cursor["added_members"]

    def pending_members(self, admin_id):
        cursor = self.collection_admin.find_one({"_id": admin_id})
        return cursor["pending_members"]

    def permit(self, member_id, member_email, admin_id, admin_name):
        self.remove_member_from_pending_members(admin_id, member_id)
        self.add_member_to_added_members(admin_id, member_id)
        se.send_email('attsystem393@gmail.com', 'eecs_393',
                      member_email, admin_name, admin_id, False)
        return True

    def reject(self, member_id, member_email, admin_id, admin_name):
        self.remove_member_from_pending_members(admin_id, member_id)
        se.send_email('attsystem393@gmail.com', 'eecs_393',
                      member_email, admin_name, admin_id, False)
        return True
