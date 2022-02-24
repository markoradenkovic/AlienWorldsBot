# IMPORTS
import time
import pyautogui
import pygetwindow
from help_scripts import browser_window_handler as bwh
from help_scripts import web_element_handler as weh
from help_scripts import region_handler as rh


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
    region = (bot.pyget_chrome_window.topleft[0], bot.pyget_chrome_window.topleft[1], bot.pyget_chrome_window.width,
              bot.pyget_chrome_window.height)
    print("BOT MINING BUTTON REGION: ", region)
    bot.pyget_chrome_window.minimize()
    time.sleep(0.2)
    bot.pyget_chrome_window.restore()
    mine_button_location = None
    mine_button_delay_counter = 0
    while mine_button_delay_counter < 5:
        time.sleep(0.5)
        mine_button_delay_counter += 0.5
        mine_button_location = pyautogui.locateOnScreen('data/images/mine-button.png', region=region, confidence=0.8)
    time.sleep(0.5)
    if mine_button_location is not None:
        print("BOT MINING BUTTON LOCATION VALUE: ", mine_button_location)
        mine_button_point = pyautogui.center(mine_button_location)
        time.sleep(0.5)
        pyautogui.click(mine_button_point[0], mine_button_point[1])
    else:
        print("MINING BUTTON NOT FOUND, MOVING ON...")


# SEQUENCE ORDER 2
def locate_and_press_claim_button(bot):
    pass


# If new window found, retrieve the guid, wait and locate the "Approve" button and press it.
def retrieve_approve_transaction_window_and_approve(bot):
    pass
