# IMPORTS
import traceback

from help_scripts import web_element_handler
from help_scripts import browser_window_handler
import time


# SEQUENCE OF DECISIONS TO MAKE IN ORDER OF 1 - 7

# SEQUENCE ORDER: 1
def open_aliens_world_website(bot):
    bot.driver.get(url='https://play.alienworlds.io/')


# SEQUENCE ORDER: 2
def press_button_start_now(bot):
    # 1. Wait for button to show up
    time.sleep(2.5)
    web_element = web_element_handler.retrieve_element_by_xpath(bot.driver,
                                                                r'/html/body/div/div[3]/div/div[1]/div')
    web_element.click()


# SEQUENCE ORDER: 3
def locate_and_press_login_button_to_redirect(bot):
    # Loopa sålänge det nya fönstret inte finns i driver.window_handles
    while len(bot.driver.window_handles) < 2:
        time.sleep(2)

    # Before clicking and opening new window
    # Store all previous existing GUIDs in the bot's memory
    # This makes sure, SEQUENCE 4 will work properly
    bot.update_previous_guids_list(
        updated_list=browser_window_handler.get_previous_selenium_driver_windows_guid(bot.driver))

    # There exists only one window from the start, parent_guid
    # As long as guid is not equal to parent_guid, it is the new window with the login-redirect button
    for guid in bot.previous_existing_guids:
        if guid != bot.parent_guid:
            bot.driver.switch_to.window(guid)  # switch to the guid
            break  # break the loop
    web_element = web_element_handler.retrieve_element_by_xpath(bot.driver,
                                                                r'/html/body/div/div/section/div['
                                                                r'2]/div/div/button/div')
    web_element.click()


# SEQUENCE ORDER: 4
def locate_sign_in_window_guid(bot):
    # Find and assign sign_in_window_guid to the bot
    succeeded = False
    try:
        while len(bot.driver.window_handles) < 3:
            time.sleep(2)
        bot.set_sign_in_window_guid(browser_window_handler.get_new_selenium_driver_window_guid(bot.driver,
                                                                                               bot.previous_existing_guids))
        bot.driver.switch_to.window(bot.sign_in_window_guid)
        succeeded = True
    except:
        print(traceback.print_exc())
    finally:
        print('Succeeded:  ', succeeded)


# SEQUENCE ORDER: 5
def input_username_credential(bot):
    time.sleep(1)
    web_element = web_element_handler.retrieve_element_by_xpath(bot.driver, '/html/body/div[1]/div/div/div/div['
                                                                            '5]/div/div/div/div[1]/div[1]/input')
    print("VALUE OF USERNAME TEXTFIELD WEB_ELEMENT: ", web_element)
    time.sleep(1)
    web_element.send_keys(bot.username)


# SEQUENCE ORDER: 6
def input_password_credential(bot):
    time.sleep(1)
    web_element = web_element_handler.retrieve_element_by_xpath(bot.driver, '/html/body/div[1]/div/div/div/div['
                                                                            '5]/div/div/div/div[1]/div[2]/input')
    print("VALUE OF PASSWORD TEXTFIELD WEB_ELEMENT: ", web_element)
    time.sleep(1)
    web_element.send_keys(bot.password)


# SEQUENCE ORDER: 7
def complete_login_process(bot):
    web_element = web_element_handler.retrieve_element_by_xpath(bot.driver, '/html/body/div[1]/div/div/div/div['
                                                                            '5]/div/div/div/div[4]/button')
    print("VALUE OF LOGIN_BUTTON WEB_ELEMENT: ", web_element)

    while web_element.is_enabled() is False:
        time.sleep(0.5)
    web_element.click()
