# IMPORTS
import pygetwindow
from helping_scripts import json_handler
from data_models.account import Account
from data_models.alien_bot import AlienBot
from program_logic.bot_runnable import BotRunnable
import helping_scripts.chrome_driver_handler as cd_handler


# ProgramInitializer CLASS
# Read all accounts from json config file
# Create separate chrome instances for each account found
# Create one instance of BotRunnable for each account found, containing both account & chrome data
# Return a list of all BotRunnables to main.py
class ProgramInitializer:
    def __init__(self):
        self.bot_runnables_list = []  # [ BotRunnableInstance, BotRunnableInstance ]
        self.alien_bots_list = []  # [ AlienBotModel, AlienBotModel, AlienBotModel ]
        self.accounts_list = []
        self.previous_chrome_windows = []  # USE CASE: helps keep track when new Chrome Windows are created
        self.new_chrome_port = 8001

    def initialize(self):
        self.read_accounts()
        cd_handler.remove_all_existing_instances()  # Delete previous chrome instances
        self.previous_chrome_windows = pygetwindow.getWindowsWithTitle(
            'Chrome')  # fill start value for previous_chrome_ids
        self.create_chrome_instances()
        self.initialize_bot_runnables()
        print("---\nProgram Initialization Successful...")
        pass

    def read_accounts(self):
        print("---\nACCOUNTS_CONFIGS_LIST")
        json_list = json_handler.read_json_file('account_configs/account_configs.json')
        for item in json_list:
            self.accounts_list.append(Account(item['username'], item['password']))
            print(item)

    def create_chrome_instances(self):
        print("---\nBeginning creating chrome instances...\n")
        for account in self.accounts_list:
            driver = cd_handler.start_chrome(self.new_chrome_port)
            chrome_window = self.get_new_chrome_window()
            # print(type(driver))
            self.alien_bots_list.append(AlienBot(driver, driver.current_window_handle, chrome_window, account))
            self.new_chrome_port += 1  # Increment port to prepare creation of next Chrome Window
        print("\nSuccessfully created chrome_instances & created AlienBot data models")

    def get_new_chrome_window(self):
        new_chrome_window = None
        current_chrome_ids = pygetwindow.getWindowsWithTitle('Chrome')
        for chrome_id in current_chrome_ids:
            if chrome_id not in self.previous_chrome_windows:
                new_chrome_window = chrome_id
        # Before returning the Chrome Window, update previous_chrome_windows list with the newly created window
        self.previous_chrome_windows.append(new_chrome_window)
        print("New Chrome Window Found: " + str(new_chrome_window))
        return new_chrome_window

    def initialize_bot_runnables(self):
        # Create new BotRunnable instances from AlienBots and append to bot_runnables_list
        for alien_bot_model in self.alien_bots_list:
            self.bot_runnables_list.append(BotRunnable(alien_bot_model))

    # This function will be called by main.py
    def get_bot_runnables(self):
        return self.bot_runnables_list
