# IMPORTS
import time
import traceback

import pyautogui
from help_scripts import browser_window_handler as bwh
from help_scripts import web_element_handler as weh


# Call this function every 10 seconds for each bot
# Try to locate the "Mine" button, if found then press it
# If "Mine" Button not found, look for "Claim Mine" button, if button found click it
# After "Claim Mine" button clicked, wait 3seconds, then check if a new "Approve Transaction" Window opened.
# If "Approve Transaction" window opened, retrieve guid and wait 1sec, then look for "Approve" Button and click it.
# If Approve Button successfully pressed, try to mine again. If neither [Mine], [Claim-Mine] button found, exit function
# And let the thread go to other bots


# START OF MINING SEQUENCE

# SEQUENCE ORDER 1
def locate_and_press_mine_button(bot):
    try:
        region = (bot.pyget_chrome_window.topleft[0], bot.pyget_chrome_window.topleft[1], bot.pyget_chrome_window.width,
                  bot.pyget_chrome_window.height)
        print("BOT MINING BUTTON REGION: ", region)
        bot.pyget_chrome_window.minimize()
        time.sleep(0.2)
        bot.pyget_chrome_window.restore()
        mine_button_location = None
        mine_button_delay_counter = 0
        while mine_button_delay_counter < 7:
            time.sleep(1)
            mine_button_delay_counter += 1
            mine_button_location = pyautogui.locateOnScreen('data/images/mine-button.png', region=region,
                                                            confidence=0.8)
            if mine_button_location is not None:
                break
        time.sleep(0.5)
        if mine_button_location is not None:
            print("BOT MINING BUTTON LOCATION VALUE: ", mine_button_location)
            mine_button_point = pyautogui.center(mine_button_location)
            time.sleep(0.5)
            pyautogui.click(mine_button_point[0], mine_button_point[1])
            print(f"COMPLETED locate_and_press_mine_button for [{bot.username}]")
        else:
            print("MINING-BUTTON NOT FOUND, MOVING ON...")
    except:
        print(f"FAILED locate_and_press_mine_button for [{bot.username}]")
        print(traceback.print_exc())


# SEQUENCE ORDER 2
def locate_and_press_claim_button(bot):
    try:
        region = (bot.pyget_chrome_window.topleft[0], bot.pyget_chrome_window.topleft[1], bot.pyget_chrome_window.width,
                  bot.pyget_chrome_window.height)
        print("BOT CLAIM MINE BUTTON REGION: ", region)
        bot.pyget_chrome_window.minimize()
        time.sleep(0.2)
        bot.pyget_chrome_window.restore()
        claim_mine_button_location = None
        claim_mine_button_delay_counter = 0
        pyautogui.moveTo(15, 15)  # Move mouse from previous position in order to remove potential side effects
        while claim_mine_button_delay_counter < 7:
            time.sleep(1)
            claim_mine_button_delay_counter += 1
            claim_mine_button_location = pyautogui.locateOnScreen('data/images/claim-mine-button.png', region=region,
                                                                  confidence=0.8)
            if claim_mine_button_location is not None:
                break
        time.sleep(0.5)
        if claim_mine_button_location is not None:
            print("BOT CLAIM MINING BUTTON LOCATION VALUE: ", claim_mine_button_location)
            claim_mine_button_point = pyautogui.center(claim_mine_button_location)
            time.sleep(0.5)
            # Update previous_existing_guids list before clicking and maybe opening new window
            bot.update_previous_guids_list(bwh.get_previous_selenium_driver_windows_guid(bot.driver))
            pyautogui.click(claim_mine_button_point[0], claim_mine_button_point[1])
            print(f"COMPLETED locate_and_press_claim_button for [{bot.username}]")
        else:
            print("CLAIM-MINING-BUTTON NOT FOUND, MOVING ON...")
    except:
        print(f"FAILED locate_and_press_claim_button for [{bot.username}]")
        print(traceback.print_exc())


# If new window found, retrieve the guid, wait and locate the "Approve" button and press it.
def retrieve_approve_transaction_window_and_approve(bot):
    try:
        approve_window_delay_counter = 0
        window_found = False
        while approve_window_delay_counter < 7:
            if len(bot.driver.window_handles) < 2:
                time.sleep(1)
                approve_window_delay_counter += 1
            else:
                window_found = True
                break
        if window_found:
            print("APPROVE-TRANSACTION-WINDOW FOUND, MOVING ON TO CLICK")
            bot.set_approve_transaction_window_guid(bwh.get_new_selenium_driver_window_guid(
                bot.driver, bot.previous_existing_guids))
            bot.driver.switch_to.window(bot.approve_transaction_window_guid)
            time.sleep(1)
            web_element = weh.retrieve_element_by_xpath(bot.driver,
                                                        '/html/body/div/div/section/div[2]/div/div[5]/button')
            print("VALUE OF APPROVE_BUTTON WEB_ELEMENT: ", web_element)
            web_element.click()
            print(f"COMPLETED retrieve_approve_transaction_window_and_approve for [{bot.username}]")
        else:
            print("APPROVE-TRANSACTION-WINDOW NOT FOUND, MOVING ON...")
    except:
        print(f"FAILED retrieve_approve_transaction_window_and_approve for [{bot.username}]")
        print(traceback.print_exc())
