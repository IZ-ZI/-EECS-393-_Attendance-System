class WaitList:

    def __init__(self):
        self.wait_list = {}

    def get_list(self):
        return self.wait_list

    def put_admin_in(self, administrator) -> bool:
        if administrator not in self.wait_list.keys():
            self.wait_list[administrator] = {}
            return True
        else:
            return False

    def put_member_in(self, member, administrator) -> bool:
        if self.is_admin_in(administrator):
            if not self.is_member_in(member, administrator):
                # 0 for initial, 1 for permit, 2 for reject
                self.wait_list.get(administrator)[member] = 0
                return True
        else:
            return False

    def pending_members(self, administrator) -> {}:
        return self.wait_list.get(administrator).keys()

    def is_member_permitted(self, member, administrator) -> bool:
        return self.get(administrator).get(member) == 1

    def delete(self, member, administrator):
        del self.wait_list.get(administrator)[member]

    def permit(self, member, administrator):
        if self.is_member_in(member, administrator):
            self.wait_list.get(administrator)[member] = 1

    def reject(self, member, administrator):
        if self.is_member_in(member, administrator):
            self.wait_list.get(administrator)[member] = 2

    def is_member_in(self, member, administrator) -> bool:
        return member in self.wait_list.get(administrator).keys()

    def is_admin_in(self, administrator) -> bool:
        return administrator in self.wait_list.keys()
