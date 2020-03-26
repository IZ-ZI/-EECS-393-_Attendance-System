from Member import Member


class MemberDatabase:
    def __init__(self):
        self.database = []
        self.wait_list = []

    def is_present(self, member_id):
        for i in self.database:
            if i.get_id() == member_id:
                return True
            # else keep searching

        # nothing found with same id if next line is reached
        return False

    def add(self, member):
        if not self.is_present(member.get_id):
            self.database.append(member)
            return True
        else:
            return False

    def update(self, member):
        for i in self.database:
            if i.get_id() == member.get_id():
                self.database.remove(i)
                self.database.append(member)
                return True
        return False

    def retrieve(self, member_id):
        if len(self.database) == 0:
            print("Nothing is in the database")
            return None
        for i in self.database:
            if i.get_id() == member_id:
                return i

        print("The member with the ID:", member_id, " is not in the database.")
        return None

    def delete(self, member_id):
        for i in self.database:
            if i.get_id() == member_id:
                self.database.remove(i)
                return True

        return False

    def login(self, member_id, password) -> Member:
        if not self.is_present(member_id):
            return None

        member = self.retrieve(member_id)
        if member.get_password() == password:
            return member
        else:
            return None

    def permit_pending_member(self, member_id) -> Member:
        for i in self.wait_list:
            if i.get_id() == member_id:
                self.database.append(i)
                self.wait_list.remove(i)
                return i

        # The member is not in wait list if lines below are reached
        return None

    def reject_pending_member(self, member_id) -> Member:
        for i in self.wait_list:
            if i.get_id() == member_id:
                removing_member = i
                self.wait_list.remove(i)
                return removing_member

        # The member is not in wait list if lines below are reached
        return None
