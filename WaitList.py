class WaitList:

    def __init__(self):
        self.wait_list = {}

    def create_wait_list(self, administrator) -> bool:
        if administrator not in self.wait_list.keys():
            self.wait_list[administrator] = {}
            return True
        else:
            return False

    def request_permit(self, member, administrator) -> bool:
        if self.is_admin_in(administrator):
            if not self.is_member_in(member, administrator):
                self.wait_list.get(administrator)[member] = False
                return True
        else:
            return False

    def member_in(self, administrator) -> {}:
        return self.get(administrator)

    def is_member_permitted(self, member, administrator) -> bool:
        return self.get(administrator).get(member)

    def delete(self, member, administrator):
        del self.wait_list.get(administrator)[member]

    def permit(self, member, administrator):
        if self.is_member_in(member, administrator):
            self.wait_list.get(administrator)[member] = True
            self.delete(member, administrator)

    def reject(self, member, administrator):
        if self.is_member_in(member, administrator):
            self.delete(member, administrator)

    def is_member_in(self, member, administrator) -> bool:
        return member in self.wait_list.get(administrator).keys()

    def is_admin_in(self, administrator) -> bool:
        return administrator in self.wait_list.keys()
