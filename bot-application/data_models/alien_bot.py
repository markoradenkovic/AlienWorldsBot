# Data Model CLASS for AlienWorlds Game Bot
# This model class stores all data necessary to identify and handle
# each separate alien-bot in the program
class AlienBot:
    def __init__(self, driver, chrome_window, account):
        self.driver = driver
        self.chrome_window = chrome_window
        self.account = account

    def __str__(self):
        return f'Bot Driver: {self.driver} AND Bot WindowID: {self.chrome_window} ' \
               f'AND Bot Username: {self.account.get_username} AND Bot Password: {self.account.get_password} '

    def get_driver(self):
        return self.driver

    def get_chrome_window(self):
        return self.chrome_window

    def get_username(self):
        return self.account.get_username()

    def get_password(self):
        return self.account.get_password()


