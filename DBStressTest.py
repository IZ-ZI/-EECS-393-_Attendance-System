from DBController import DBController
from pymongo import MongoClient
from Member import Member
from Administrator import Administrator
from Activity import Activity

cluster = MongoClient(
    "mongodb+srv://wz:1999314Zwh%2F@attendancemanagementsystem-7immk.mongodb.net/test?retryWrites=true&w"
    "=majority")
db = cluster["AMS"]
collection_member = db["Member"]
collection_admin = db["Administrator"]
collection_activity = db["Activity"]

db_controller = DBController(collection_member, collection_admin, collection_activity)

# for i in range (0, 100):
#      member = Member(str(i), str(i), "member@gmail.com", "member")
#      db_controller.add_member(member)

# for i in range (0 ,100):
#      member = Member("updated name", str(i), "updated email", "updated password")
#      db_controller.update_member(member)

# for i in range (0 ,100):
#     db_controller.retrieve_member(str(i))

# for i in range (0 ,100):
#      db_controller.delete_member(str(i))


# for i in range (0 ,100):
#      db_controller.delete_member(str(i))


# for i in range (0, 100):
#     admin = Administrator(str(i), str(i), "admin@gmail.com", "admin")
#     db_controller.add_admin(admin)

# for i in range (0 ,100):
#     admin = Administrator("updated name", str(i), "updated email", "updated password")
#     db_controller.update_admin(admin)
#

# for i in range (0 ,100):
#      db_controller.retrieve_admin(str(i))


# for i in range (0 ,100):
#       db_controller.delete_admin(str(i))


# for i in range (0, 100):
#     activitiy = Activity(str(i), str(i), "start_time", "end_time", "location")
#     db_controller.add_activity(activitiy, "0")


# for i in range (0 ,100):
#      activity = Activity( str(i), str(i), "updated start_time", "updated end_time", "updated location")
#      db_controller.update_activity(activity)

# for i in range (0 ,100):
#      db_controller.retrieve_activity(str(i))

# for i in range (0 ,100):
#         db_controller.delete_activity(str(i))
#

# for i in range (0 ,100):
#     db_controller.add_club_to_member(str(i), "0")


# for i in range (0 ,100):
#    db_controller.remove_club_from_member(str(i), "0")

# for i in range (0, 100):
#     db_controller.add_member_to_pending_members("0", str(i))

# for i in range (0 ,100):
#     db_controller.remove_member_from_pending_members("0", str(i))

# for i in range (0, 100):
#     db_controller.add_member_to_added_members("0", str(i))

# for i in range (0 ,100):
#     db_controller.remove_member_from_added_members("0", str(i))


# for i in range (0 ,100):
#     db_controller.add_activity_to_member("0", str(i), "0", "late")

# for i in range (0 ,100):
#     db_controller.set_member_activity_status("0", str(i), "0", "on_time")

# for i in range(0, 100):
#     db_controller.remove_activity_from_member("0", str(i), "0")


# for i in range (0 ,100):
#       db_controller.add_activity_to_admin(str(i), "0")


# for i in range (0 ,100):
#       db_controller.remove_activity_from_admin(str(i), "0")










