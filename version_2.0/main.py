# IMPORTS
from help_scripts import json_handler
from help_scripts import chrome_instance_handler
from bot import Bot

# STEP 1: Read Account Data
accounts_list = json_handler.read_json_file('data/configs/accounts.json')

# https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
print('___\nACCOUNTS RETRIEVED FROM CONFIGS: ')
print(*accounts_list, sep='\n')


# STEP 2: Initialize Bots with Account Data
bots_list = []
for account in accounts_list:
    bots_list.append(Bot(account['username'], account['password']))

print('\n___\nBOTS INITIALIZED WITH ACCOUNT DATA: ')
print(*bots_list, sep='\n')

# STEP 3: Setup Chrome Instances for Bots
port = 36734
chrome_instance_handler.remove_all_existing_instances()
for bot in bots_list:
    bot.setup_chrome_instance(port)
    port += 1

# STEP 4: Prepare Bots for Mining
for bot in bots_list:
    bot.start_preparation_sequence()

# STEP 5: Command Bots to Start Mining

