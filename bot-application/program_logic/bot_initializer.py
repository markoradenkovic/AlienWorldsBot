# IMPORTS
import helping_scripts.webdriver_element_handler as web_element_handler
import helping_scripts.browser_window_handler as window_handler
import time


# BotInitializer CLASS
# This class handles automation all the way until
# the bot is successfully logged in and ready to play / mine AlienWorlds Game
class BotInitializer:
    def __init__(self, alien_bot_model):
        self.driver = alien_bot_model.get_driver()
        self.username = alien_bot_model.get_username()
        self.password = alien_bot_model.get_password()
        self.parent_GUID = alien_bot_model.get_parent_guid()  # Main Driver Window GUID
        self.previous_windows_guid = []  # helps keep track when new Chrome Windows are created with driver
        self.sign_in_window_guid = None

    def start(self):
        self.open_aliens_world_website()
        self.press_button_start_now()
        self.locate_and_press_login_button_to_redirect()
        self.locate_sign_in_window_guid()
        self.input_username_credential()
        self.input_password_credential()
        self.complete_login_process()

    def open_aliens_world_website(self):
        self.driver.get(url='https://play.alienworlds.io/')
        print("---\nOpened Aliens World Website For Bot")

    def press_button_start_now(self):
        # 1. Wait for button to show up
        web_element = web_element_handler.retrieve_element_by_xpath(self.driver,
                                                                    r'/html/body/div/div[3]/div/div[1]/div')
        # 2. Click the button
        web_element.click()

    def locate_and_press_login_button_to_redirect(self):
        time.sleep(2)
        allGUID = self.driver.window_handles  # Retrieve all existing GUIDs
        print("Page title before Switching : " + self.driver.title)
        print("Total Windows : " + allGUID.size())
        for guid in allGUID:
            if guid != self.parent_GUID:
                self.driver.switch_to_window(guid)  # switch to the guid
                break  # break the loop


    def locate_sign_in_window_guid(self):
        # Find and assign sign_in_window_guid to class member variable
        pass

    def input_username_credential(self):
        pass

    def input_password_credential(self):
        pass

    def complete_login_process(self):
        pass
