import json


# https://www.pythonforbeginners.com/files/with-statement-in-python
# https://www.geeksforgeeks.org/read-json-file-using-python/

def read_json_file(file_path):
    with open(file=file_path, mode='r') as file:
        account_configs = json.load(file)
        return account_configs
