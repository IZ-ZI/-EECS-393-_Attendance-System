class Member(object):
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def get_name(self):
        return self.name

    def get_id(self):
        return self.ID
