# IMPORTS
import helping_scripts.webdriver_element_handler as web_element_handler


# BotInitializer CLASS
# This class handles automation all the way until
# the bot is successfully logged in and ready to play / mine AlienWorlds Game
class BotInitializer:
    def __init__(self, alien_bot_model):
        self.driver = alien_bot_model.get_driver()
        self.chrome_window = alien_bot_model.get_chrome_window()
        self.username = alien_bot_model.get_username()
        self.password = alien_bot_model.get_password()
        self.previous_wax_windows = []

    def start(self):
        self.open_aliens_world_website()
        self.press_button_start_now()
        self.locate_and_press_login_button()

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
        pass

    def locate_sign_in_window(self):
        pass

    def input_login_credentials(self):
        pass

    def complete_login_process(self):
        pass


