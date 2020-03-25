import MemberDatabase
import Waitlist


class Driver:
    def __init__(self, member_database: MemberDatabase, waitlist: Waitlist):
        self.member_database = member_database
        self.waitlist = waitlist
