class AccessPermissions:
    def __init__(self):
        self.permissions = {}

    def set_permission(self, document, user, level):
        self.permissions[document] = {user: level}
        return self.permissions
