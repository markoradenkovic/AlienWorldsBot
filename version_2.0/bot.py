# IMPORTS

class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = None
        self.parent_guid = None
        self.pyget_chrome_window = None

    def __str__(self):
        return f'BOT DETAILS: \nUsername: {self.username}, Password: {self.password}'

    def setup_chrome_instance(self):
        # Call Decisions in Order and Log to Console
        pass

    def prepare_for_mining(self):
        # Call Decisions in Order and Log to Console
        pass

    def start_mining(self):
        # Call Decisions in Order and Log to Console
        pass




