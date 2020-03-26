from MemberDatabase import MemberDatabase
from WaitList import WaitList
import sendEmail as sE


class Administrator:
    def __init__(self, organization_id: str, organization_name: str, email_address: str, password: str,
                 wait_list: WaitList):
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.email_address = email_address
        self.password = password
        self.memberDatabase = MemberDatabase()
        self.wait_list = wait_list

    def create_wait_list(self):
        self.wait_list.put_admin_in(self)

    def get_organization_id(self) -> str:
        return self.organization_id

    def get_organization_name(self) -> str:
        return self.organization_name

    def get_wait_list(self) -> WaitList:
        return self.wait_list

    def get_member_database(self) -> MemberDatabase:
        return self.memberDatabase

    def get_email_adderss(self) -> str:
        return self.email_address

    def get_password(self) -> str:
        return self.password

    def delete_member(self, member_id) -> bool:
        self.memberDatabase.delete(member_id)

    def add_member(self, member) -> bool:
        self.memberDatabase.update(member)

    def members_in_wait_list(self):
        self.wait_list.pending_members(self)

    def permit(self, member):
        self.wait_list.permit(member, self)
        self.memberDatabase.add(member)
        se.send_email(self.email_address, 'placeholder', member.get_email_adderss)

    def reject(self, member):
        self.wait_list.reject(member, self)
        se.send_email(self.email_address, 'placeholder', member.get_email_adderss)
