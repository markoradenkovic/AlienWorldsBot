# IMPORTS
from program_logic.bot_initializer import BotInitializer
from program_logic.bot_miner import BotMiner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# BotRunnable CLASS
# Has info about the AlienBot Model which has all necessary Account and Chrome Window data
#
# Has access to BotInitializer, which handles automation all the way until
# the bot is successfully logged in and ready to play AlienWorlds Game
#
# Has access to BotMiner, which handles all logic about mining. When all bots are ready,
#
# main.py will loop and call 'start_mining()' every 10seconds for each BotRunnable to make sure all bots are mining 24/7
class BotRunnable:
    def __init__(self, alien_bot_model):
        self.alien_bot_instance = alien_bot_model
        self.bot_initializer_instance = BotInitializer(alien_bot_model)
        self.bot_miner_instance = BotMiner()

    def prepare_bot_for_mining(self):
        print("Prepare BOT FOR MINING")
        # Use instance of BotInitalizer class
        self.bot_initializer_instance.start()

    def start_mining(self):
        # Use instance of BotMiner class
        print("START MINING")
