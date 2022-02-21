# IMPORTS
from help_scripts import chrome_instance_handler


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = None
        self.parent_guid = None
        self.pyget_chrome_window = None

    def __str__(self):
        return f'BOT DETAILS: \nUsername: {self.username}, Password: {self.password}'

    def setup_chrome_instance(self, port):
        # Call Decisions in Order and Log to Console
        print(f'SETTING UP CHROME INSTANCE FOR {self.username}')
        chrome_data_dict = chrome_instance_handler.start_chrome_and_retrieve_windows(port)
        self.driver = chrome_data_dict['driver']
        self.parent_guid = chrome_data_dict['driver_parent_guid']
        self.pyget_chrome_window = chrome_data_dict['pyget_chrome_window']
        print(f'SUCCESSFULLY CONFIGURED CHROME INSTANCE FOR USER: \'{self.username}\'')

    def prepare_for_mining(self):
        # Call Decisions in Order and Log to Console
        pass

    def start_mining(self):
        # Call Decisions in Order and Log to Console
        pass
