from user import User


class Admin(User):
    def __init__(self, first_name, last_name, privileges=None):
        super(Admin, self).__init__(first_name=first_name, last_name=last_name)
        self.privileges = Privilege(privileges)


class Privilege:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = privileges

    def show_privileges(self):
        return self.privileges


print("&&&&&&&&&&&&&&&&&")
admin = Admin('aaa', 'bbb', ['can edit post'])
admin.privileges.show_privileges()
admin.describe_user()
print(admin.privileges.show_privileges())
