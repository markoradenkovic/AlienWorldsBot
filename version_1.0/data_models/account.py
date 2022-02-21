# Data Model Class for Accounts
class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f'Account Username: {self.username} AND Account Password: {self.password}'

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

