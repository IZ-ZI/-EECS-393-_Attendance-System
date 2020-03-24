class WaitList:

    def __init__(self):
        self.wait_list = {}

    def create_wait_list(self, administrator) -> bool:
        if administrator not in self.wait_list.keys():
            self.wait_list[administrator] = []
            return True
        else:
            return False

    def request_permit(self, member, administrator) -> bool:
        if administrator in self.wait_list.keys():
            self.wait_list.get(administrator).append(member)
            return True
        else:
            return False