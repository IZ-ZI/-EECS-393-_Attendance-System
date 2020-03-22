class MemberDatabase(object):
    def __int__(self):
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


