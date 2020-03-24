from MemberDatabase import MemberDatabase
class Administrator:
    def __init__(self, organization_id, organization_name):
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.memberDatabase = MemberDatabase()


    def get_organization_id(self) -> int:
        return self.organization_id

    def get_organization_name(self) -> str:
        return self.organization_name

    def delete_member(self, member_id) -> bool:
        self.memberDatabase.delete(member_id)

    def add_member(self, member_id):
        self.memberDatabase.update(member_id)





