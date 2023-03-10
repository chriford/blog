from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'create_blog': True,
        'update_blog':True,
        'delete_blog':True,
        'view_blog':True,
        'make_donation':True,
    }

