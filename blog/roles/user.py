from rolepermissions.roles import AbstractUserRole

class User(AbstractUserRole):
    available_permissions = {
        'view_blog':True,
        'make_donation':True,
    }