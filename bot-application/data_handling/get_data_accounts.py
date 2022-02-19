import json


def read_accounts():
    with open(file='data_handling/account_configs.json', mode='r') as file:
        account_configs = json.load(file)
        return account_configs
