import pygetwindow
from old_shit_delete_later.data_handling import get_data_accounts
from helping_scripts import webdriver_element_handler, chrome_driver_handler
from old_shit_delete_later.data_models import bot_instance


class BotCoreDecisions:
    def __init__(self):
        self.active_chrome_ids = []
        self.retrieved_chrome_ids = []
        self.accounts_list = {}
        self.bot_instances = []

    def start_bot(self):
        executing_chrome.remove_all_existing_instances()
        self.initiate_accounts()
        self.initiate_chrome_instances()

    def initiate_accounts(self):
        self.accounts_list = get_data_accounts.read_accounts()

    # Create a list with both the [driver, window_id, username, password]
    def initiate_chrome_instances(self):
        self.active_chrome_ids = pygetwindow.getWindowsWithTitle('Chrome')
        driver = executing_chrome.start_chrome(port='8001')
        self.retrieved_chrome_ids = pygetwindow.getWindowsWithTitle('Chrome')
        print(self.active_chrome_ids)
        print(self.retrieved_chrome_ids)
        new_chrome_window_id = self.find_new_chrome_window()
        self.active_chrome_ids.append(new_chrome_window_id)
        self.bot_instances.append(
            bot_instance.BotInstance(
                driver,
                new_chrome_window_id,
                self.accounts_list['account1']['username'],
                self.accounts_list['account1']['password']
            ))
        help_functions.print_list_to_console(self.bot_instances)

    def find_new_chrome_window(self):
        for id in self.retrieved_chrome_ids:
            if id not in self.active_chrome_ids:
                return id

    def start_alien_worlds(self):
        pass

    def login_with_accounts(self):
        pass

    def start_mining(self):
        pass
