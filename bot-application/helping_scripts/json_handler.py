import json


def read_json_file(file_path):
    # 'data_handling/account_configs.json'
    with open(file=file_path, mode='r') as file:
        account_configs = json.load(file)
        return account_configs
