from MemberDatabase import MemberDatabase
class Administrator:
    def __init__(self, organization_id, organization_name, wait_list):
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.memberDatabase = MemberDatabase()
        self.wait_list = wait_list
        self.wait_list.create_wait_list(self)

    def get_organization_id(self) -> int:
        return self.organization_id

    def get_organization_name(self) -> str:
        return self.organization_name

    def delete_member(self, member_id) -> bool:
        self.memberDatabase.delete(member_id)

    def add_member(self, member) -> bool:
        self.memberDatabase.update(member)

    def members_in_wait_list(self):
        self.wait_list.member_in(self)

    def permit(self, member):
        self.wait_list.permit(member, self)

    def reject(self, member):
        self.wait_list.reject(member, self)











