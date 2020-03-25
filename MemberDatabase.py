class MemberDatabase:
    def __init__(self):
        self.database = []

    def is_present(self, member_id):
        for i in self.database:
            if i.get_id() == member_id:
                return True
            else:
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
        for i in self.database:
            if i.get_id() == member_id:
                return i

        print("This member is not in the database.")

    def delete(self, member_id):
        for i in self.database:
            if i.get_id() == member_id():
                self.database.remove(i)
                return True

        return False
