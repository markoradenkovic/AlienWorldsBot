# IMPORTS
import helping_scripts.webdriver_element_handler as web_element_handler
import helping_scripts.browser_window_handler as window_handler
import pyautogui
import pygetwindow
import helping_scripts.chrome_driver_handler as cd_handler
import time
import pyperclip  # Used for putting something in the copied clip in the pc


# BotInitializer CLASS
# This class handles automation all the way until
# the bot is successfully logged in and ready to play / mine AlienWorlds Game
class BotInitializer:
    def __init__(self, alien_bot_model):
        self.driver = alien_bot_model.get_driver()
        self.chrome_window = alien_bot_model.get_chrome_window()
        self.username = alien_bot_model.get_username()
        self.password = alien_bot_model.get_password()
        self.previous_chrome_windows = []  # USE CASE: helps keep track when new Chrome Windows are created
        self.previous_wax_windows = []
        self.sign_in_window = None

    def start(self):
        self.open_aliens_world_website()
        self.press_button_start_now()
        self.locate_and_press_login_button_to_redirect()
        # self.locate_sign_in_window()
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
        # Find new window
        # new_window = None
        # while new_window is None:
        #     time.sleep(0.5)
        #     new_window = window_handler.get_new_browser_window("WAX", self.previous_wax_windows)
        # self.previous_wax_windows.append(new_window)

        login_redirect_button_location = None
        while login_redirect_button_location is None:
            time.sleep(0.5)
            login_redirect_button_location = pyautogui.locateOnScreen('images/wax-login-redirect.png')
        print("Login-Redirect-Button Coordinates:\n" + str(login_redirect_button_location))
        pyautogui.click(login_redirect_button_location[0], login_redirect_button_location[1])

    # def locate_sign_in_window(self):
    #     # Find new window
    #     # self.sign_in_window = ...
    #     pass

    def input_username_credential(self):
        email_text_field = None
        while email_text_field is None:
            time.sleep(0.3)
            email_text_field = pyautogui.locateOnScreen('images/email-username-text-field.png')
        print("Email / Username Coordinates:\n" + str(email_text_field))
        pyautogui.click(email_text_field[0], email_text_field[1])
        splitted_email = self.username.split("@")
        pyautogui.typewrite(splitted_email[0], interval=0.05)
        pyperclip.copy('@')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.typewrite(splitted_email[1] + '\n', interval=0.05)

    def input_password_credential(self):
        password_text_field = None
        while password_text_field is None:
            time.sleep(0.3)
            password_text_field = pyautogui.locateOnScreen('images/password-text-field.png')
        print("Password Coordinates:\n" + str(password_text_field))
        pyautogui.click(password_text_field[0], password_text_field[1])
        pyautogui.typewrite(self.password + '\n', interval=0.05)

    def complete_login_process(self):
        sign_in_button = None
        while sign_in_button is None:
            time.sleep(0.3)
            sign_in_button = pyautogui.locateOnScreen('images/wax-sign-in-button.png')
            pyautogui.click(sign_in_button[0], sign_in_button[1])



