

class BotInstance:

    def __init__(self, driver, window_id, username, password):
        self.driver = driver
        self.window_id = window_id
        self.username = username
        self.password = password

    def __str__(self):
        return f'Bot Driver: {self.driver} AND Bot WindowID: {self.window_id} AND Bot Username: {self.username} AND ' \
               f'Bot Password: {self.password} '

    def get_driver(self):
        return self.driver

    def get_window_id(self):
        return self.window_id

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

