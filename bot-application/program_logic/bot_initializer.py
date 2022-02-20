# IMPORTS
import helping_scripts.webdriver_element_handler as web_element_handler
import helping_scripts.browser_window_handler as window_handler
import time
import traceback


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
        print("COMPLETED open_aliens_world_website")
        self.press_button_start_now()
        print("COMPLETED press_button_start_now")
        self.locate_and_press_login_button_to_redirect()
        print("COMPLETED locate_and_press_login_button_to_redirect")
        self.locate_sign_in_window_guid()
        print("COMPLETED locate_sign_in_window_guid")
        self.input_username_credential()
        print("COMPLETED input_username_credential")
        self.input_password_credential()
        print("COMPLETED input_password_credential")
        self.complete_login_process()
        print("COMPLETED complete_login_process")

    def open_aliens_world_website(self):
        self.driver.get(url='https://play.alienworlds.io/')
        print("---\nOpened Aliens World Website For Bot")

    def press_button_start_now(self):
        # 1. Wait for button to show up
        time.sleep(2.5)
        web_element = web_element_handler.retrieve_element_by_xpath(self.driver,
                                                                    r'/html/body/div/div[3]/div/div[1]/div')
        web_element.click()

    def locate_and_press_login_button_to_redirect(self):
        # Loopa sålänge det nya fönstret inte finns i driver.window_handles
        while len(self.driver.window_handles) < 2:
            time.sleep(2)
        self.previous_windows_guid = self.driver.window_handles  # Retrieve all existing GUIDs
        print("Page title before Switching : " + self.driver.title)
        print("Total Windows : \n" + '\n'.join(map(str, self.previous_windows_guid)))
        for guid in self.previous_windows_guid:
            if guid != self.parent_GUID:
                self.driver.switch_to.window(guid)  # switch to the guid
                break  # break the loop
        web_element = web_element_handler.retrieve_element_by_xpath(self.driver,
                                                                    r'/html/body/div/div/section/div['
                                                                    r'2]/div/div/button/div')
        web_element.click()

    def locate_sign_in_window_guid(self):
        # Find and assign sign_in_window_guid to class member variable
        succeeded = False
        try:
            while len(self.driver.window_handles) < 3:
                time.sleep(2)
            self.sign_in_window_guid = window_handler.get_new_selenium_driver_window_guid(self.driver,
                                                                                          self.previous_windows_guid)
            self.driver.switch_to.window(self.sign_in_window_guid)
            succeeded = True
        except:
            print(traceback.print_exc())
        finally:
            print('Succeeded:  ', succeeded)


    def input_username_credential(self):
        web_element = web_element_handler.retrieve_element_by_xpath(self.driver, '/html/body/div[1]/div/div/div/div['
                                                                                 '5]/div/div/div/div[1]/div[1]/input')
        web_element.send_keys(self.username)

    def input_password_credential(self):
        web_element = web_element_handler.retrieve_element_by_xpath(self.driver, '/html/body/div[1]/div/div/div/div['
                                                                                 '5]/div/div/div/div[1]/div[2]/input')
        web_element.send_keys(self.password)

    def complete_login_process(self):
        web_element = web_element_handler.retrieve_element_by_xpath(self.driver, '/html/body/div[1]/div/div/div/div['
                                                                                 '5]/div/div/div/div[4]/button')
        while web_element.is_enabled() is False:
            time.sleep(0.5)
        web_element.click()
