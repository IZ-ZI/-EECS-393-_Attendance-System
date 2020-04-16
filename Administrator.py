import sendEmail as se


class Administrator:
    def __init__(self, organization_name: str, organization_id: str, email_address: str, password: str):
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.email_address = email_address
        self.password = password

    def get_organization_id(self) -> str:
        return self.organization_id

    def get_organization_name(self) -> str:
        return self.organization_name

    def get_email_address(self) -> str:
        return self.email_address

    def get_password(self) -> str:
        return self.password


