# IMPORTS
import traceback

from HelpScripts import WebElementHandler
from HelpScripts import BrowserWindowHandler
import time


# SEQUENCE OF DECISIONS TO MAKE IN ORDER OF 1 - 7

# SEQUENCE ORDER: 1
def open_aliens_world_website(bot):
    try:
        bot.driver.get(url='https://play.alienworlds.io/')
        print(f"COMPLETED open_aliens_world_website for [{bot.username}]")
    except:
        print(f"FAILED open_aliens_world_website for [{bot.username}]")
        print(traceback.print_exc())


# SEQUENCE ORDER: 2
def press_button_start_now(bot):
    # 1. Wait for button to show up
    try:
        time.sleep(2.5)
        web_element = WebElementHandler.retrieve_element_by_xpath(bot.driver,
                                                                    r'/html/body/div/div[3]/div/div[1]/div')
        web_element.click()
        print(f"COMPLETED press_button_start_now for [{bot.username}]")
    except:
        print(f"FAILED press_button_start_now for [{bot.username}]")
        print(traceback.print_exc())


# SEQUENCE ORDER: 3
def locate_and_press_login_button_to_redirect(bot):
    try:
        # Loopa sålänge det nya fönstret inte finns i driver.window_handles
        while len(bot.driver.window_handles) < 2:
            time.sleep(2)

        # Before clicking and opening new window
        # Store all previous existing GUIDs in the bot's memory
        # This makes sure, SEQUENCE 4 will work properly
        time.sleep(2)
        bot.update_previous_guids_list(
            updated_list=BrowserWindowHandler.get_previous_selenium_driver_windows_guid(bot.driver))

        # There exists only one window from the start, parent_guid
        # As long as guid is not equal to parent_guid, it is the new window with the login-redirect button
        for guid in bot.previous_existing_guids:
            if guid != bot.parent_guid:
                bot.driver.switch_to.window(guid)  # switch to the guid
                break  # break the loop
        web_element = WebElementHandler.retrieve_element_by_xpath(bot.driver,
                                                                    r'/html/body/div/div/section/div['
                                                                    r'2]/div/div/button/div')
        web_element.click()
        print(f"COMPLETED locate_and_press_login_button_to_redirect for [{bot.username}]")
    except:
        print(f"FAILED locate_and_press_login_button_to_redirect for [{bot.username}]")
        print(traceback.print_exc())


# SEQUENCE ORDER: 4
def locate_sign_in_window_guid(bot):
    try:
        # Find and assign sign_in_window_guid to the bot
        while len(bot.driver.window_handles) < 3:
            time.sleep(2)
        bot.set_sign_in_window_guid(BrowserWindowHandler.get_new_selenium_driver_window_guid(bot.driver,
                                                                                               bot.previous_existing_guids))
        bot.driver.switch_to.window(bot.sign_in_window_guid)
        print(f"COMPLETED locate_sign_in_window_guid for [{bot.username}]")
    except:
        print(f"FAILED locate_sign_in_window_guid for [{bot.username}]")
        print(traceback.print_exc())


# SEQUENCE ORDER: 5
def input_username_credential(bot):
    try:
        time.sleep(1)
        web_element = WebElementHandler.retrieve_element_by_xpath(bot.driver, '/html/body/div[1]/div/div/div/div['
                                                                                '5]/div/div/div/div[1]/div[1]/input')
        print("VALUE OF USERNAME TEXTFIELD WEB_ELEMENT: ", web_element)
        time.sleep(1)
        web_element.send_keys(bot.username)
        print(f"COMPLETED input_username_credential for [{bot.username}]")
    except:
        print(f"FAILED input_username_credential for [{bot.username}]")
        print(traceback.print_exc())


# SEQUENCE ORDER: 6
def input_password_credential(bot):
    try:
        time.sleep(1)
        web_element = WebElementHandler.retrieve_element_by_xpath(bot.driver, '/html/body/div[1]/div/div/div/div['
                                                                                '5]/div/div/div/div[1]/div[2]/input')
        print("VALUE OF PASSWORD TEXTFIELD WEB_ELEMENT: ", web_element)
        time.sleep(1)
        web_element.send_keys(bot.password)
        print(f"COMPLETED input_password_credential for [{bot.username}]")
    except:
        print(f"FAILED input_password_credential for [{bot.username}]")
        print(traceback.print_exc())


# SEQUENCE ORDER: 7
def complete_login_process(bot):
    try:
        web_element = WebElementHandler.retrieve_element_by_xpath(bot.driver, '/html/body/div[1]/div/div/div/div['
                                                                                '5]/div/div/div/div[4]/button')
        print("VALUE OF LOGIN_BUTTON WEB_ELEMENT: ", web_element)

        while web_element.is_enabled() is False:
            time.sleep(0.5)
        web_element.click()
        print(f"COMPLETED complete_login_process for [{bot.username}]")
    except:
        print(f"FAILED complete_login_process for [{bot.username}]")
        print(traceback.print_exc())
    finally:
        input(f"Press ENTER to continue if login succeeded for [{bot.username}], Otherwise LOGIN MANUALLY, then press "
              f"ENTER")


