# IMPORTS
from HelpScripts import ChromeInstanceHandler
from bot_logic import preparation_sequence as p_sequence
from bot_logic import mining_sequence as m_sequence
import time


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = None
        self.parent_guid = None
        self.previous_existing_guids = []  # Update this list before opening new windows
        self.sign_in_window_guid = None
        self.approve_transaction_window_guid = None
        self.pyget_chrome_window = None

    def __str__(self):
        return f'\nBOT DETAILS: \nUsername: {self.username}, Password: {self.password}'

    def setup_chrome_instance(self, port):
        print(f'\n___\nSETTING UP CHROME INSTANCE FOR {self.username}')

        chrome_data_dict = ChromeInstanceHandler.start_chrome_and_retrieve_windows(port)
        self.driver = chrome_data_dict['driver']
        self.parent_guid = chrome_data_dict['driver_parent_guid']
        self.pyget_chrome_window = chrome_data_dict['pyget_chrome_window']

        print(f'\nSUCCESSFULLY CONFIGURED CHROME INSTANCE FOR USER: \'{self.username}\'')

    def start_preparation_sequence(self):
        print(f'\n___\nPREPARING MINING FOR {self.username}\n')

        # MAKE SURE THIS WINDOW IS FOCUSED
        self.pyget_chrome_window.minimize()
        time.sleep(0.2)
        self.pyget_chrome_window.restore()

        p_sequence.open_aliens_world_website(self)
        p_sequence.press_button_start_now(self)
        p_sequence.locate_and_press_login_button_to_redirect(self)
        p_sequence.locate_sign_in_window_guid(self)
        p_sequence.input_username_credential(self)
        p_sequence.input_password_credential(self)
        p_sequence.complete_login_process(self)

        print(f'\nSUCCESSFULLY PREPARED FOR MINING FOR USER: \'{self.username}\'')

    def start_mining(self):
        print(f'\n___\nSTARTED MINING PROCESS FOR {self.username}\n')
        m_sequence.close_all_windows_except_parent(self)
        m_sequence.locate_and_press_mine_button(self)
        m_sequence.locate_and_press_claim_button(self)
        m_sequence.retrieve_approve_transaction_window_and_approve(self)
        print(f'\nMINING PROCESS FINISHED FOR: \'{self.username}\'')

    def update_previous_guids_list(self, updated_list):
        self.previous_existing_guids = updated_list

    def set_sign_in_window_guid(self, window):
        self.sign_in_window_guid = window

    def set_approve_transaction_window_guid(self, window):
        self.approve_transaction_window_guid = window
