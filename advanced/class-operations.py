from modules import utilities as util


class Accounts:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def show_login_info(self):
        print(f"Username: {self.username} Password: {self.password}")

    def login_successful(self):
        print("Login successful")


class Admin(Accounts):
    def __init__(self, username, password, permission):
        super().__init__(username, password)
        self.permission = permission

    def show_permission(self):
        print(f"Permission: {self.permission}")


admin = Admin("admin", "123456", "admin")


class A:
    def method_a(self):
        print("Method A")


class B:
    def method_b(self):
        print("Method B")


class C(A, B):
    def method_c(self):
        print("Method C")


c = C()
c.method_a()
c.method_b()
c.method_c()


account = Accounts("admin", "123456")
account.show_login_info()

if account.username == "admin" and account.password == "123456":
    account.login_successful()


util.print_username("Berkay Gediz")
util.show_age(25)


calculator = util.Calculator()
print(calculator.add(2, 3))
