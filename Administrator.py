from MemberDatabase import MemberDatabase
import Member
import sendEmail as se


class Administrator:
    def __init__(self, organization_name: str, organization_id: str, email_address: str, password: str):
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.email_address = email_address
        self.password = password
        self.memberDatabase = MemberDatabase()

    def get_organization_id(self) -> str:
        return self.organization_id

    def get_organization_name(self) -> str:
        return self.organization_name

    def get_member_database(self) -> MemberDatabase:
        return self.memberDatabase

    def get_email_adderss(self) -> str:
        return self.email_address

    def get_password(self) -> str:
        return self.password

    def delete_member(self, member) -> bool:
        self.memberDatabase.delete(member.get_id())

    def add_member(self, member) -> bool:
        self.memberDatabase.add(member)

    def pend_member(self, member):
        self.memberDatabase.add_to_wait_list(member)

    def permit(self, member: Member):
        se.send_email('attsystem393@gmail.com', 'eecs_393',
                      self.memberDatabase.permit_pending_member(member.get_id()).get_email_adderss, self.get_organization_name(), self.get_organization_id(), False)
        return True

    def reject(self, member: Member):
        se.send_email('attsystem393@gmail.com', 'eecs_393',
                      self.memberDatabase.reject_pending_member(member.get_id()).get_email_address, self.get_organization_name(), self.get_organization_id(), False)
        return True
