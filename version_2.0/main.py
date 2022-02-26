# IMPORTS
import traceback

try:
    import time
    import sys
    from HelpScripts import JsonHandler
    from HelpScripts import ChromeInstanceHandler
    from bot import Bot
    import pathlib
    #
    # path = pathlib.Path(__file__).parent.resolve()
    #
    # sys.path.insert(0, f"{path}/help_scripts/json_handler.py")
    # sys.path.insert(0, f"{path}/help_scripts/chrome_instance_handler.py")


    # STEP 1: Read Account Data
    accounts_list = JsonHandler.read_json_file('data/configs/accounts.json')

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
    ChromeInstanceHandler.remove_all_existing_instances()
    for bot in bots_list:
        bot.setup_chrome_instance(port)
        port += 1

    # STEP 4: Prepare Bots for Mining
    for bot in bots_list:
        # TODO ERROR IN PREPARATION SEQUENCE WHEN USING MULTIPLE ACCOUNTS ?
        # TODO SEEMS TO BE SOLVED ???
        bot.start_preparation_sequence()
        time.sleep(2)  # Wait 2 sec before preparing next bot

    # STEP 5: Command Bots to Start Mining
    while True:
        for bot in bots_list:
            bot.start_mining()
except:
    print(traceback.print_exc())
    time.sleep(1000)