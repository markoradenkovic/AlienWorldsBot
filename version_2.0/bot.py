# IMPORTS
from help_scripts import chrome_instance_handler
from bot_logic import preparation_sequence as p_sequence


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = None
        self.parent_guid = None
        self.pyget_chrome_window = None

    def __str__(self):
        return f'\nBOT DETAILS: \nUsername: {self.username}, Password: {self.password}'

    def setup_chrome_instance(self, port):
        print(f'\n___\nSETTING UP CHROME INSTANCE FOR {self.username}')

        chrome_data_dict = chrome_instance_handler.start_chrome_and_retrieve_windows(port)
        self.driver = chrome_data_dict['driver']
        self.parent_guid = chrome_data_dict['driver_parent_guid']
        self.pyget_chrome_window = chrome_data_dict['pyget_chrome_window']

        print(f'\nSUCCESSFULLY CONFIGURED CHROME INSTANCE FOR USER: \'{self.username}\'')

    def start_preparation_sequence(self):
        print(f'\n___\nPREPARING MINING FOR {self.username}\n')

        p_sequence.open_aliens_world_website(self)
        print(f"COMPLETED open_aliens_world_website for [{self.username}]")

        p_sequence.press_button_start_now(self)
        print(f"COMPLETED press_button_start_now for [{self.username}]")

        p_sequence.locate_and_press_login_button_to_redirect(self)
        print(f"COMPLETED locate_and_press_login_button_to_redirect for [{self.username}]")

        p_sequence.locate_sign_in_window_guid(self)
        print(f"COMPLETED locate_sign_in_window_guid for [{self.username}]")

        p_sequence.input_username_credential(self)
        print(f"COMPLETED input_username_credential for [{self.username}]")

        p_sequence.input_password_credential(self)
        print(f"COMPLETED input_password_credential for [{self.username}]")

        p_sequence.complete_login_process(self)
        print(f"COMPLETED complete_login_process for [{self.username}]")

        print(f'\nSUCCESSFULLY PREPARED FOR MINING FOR USER: \'{self.username}\'')
        pass

    def start_mining(self):
        # Call Decisions in Order and Log to Console
        pass

