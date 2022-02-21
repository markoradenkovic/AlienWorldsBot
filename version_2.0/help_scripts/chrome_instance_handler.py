import os
import pathlib
import shutil
import time
import traceback
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from help_scripts import browser_window_handler as bwh

path = str(pathlib.Path(__file__).parent.parent.resolve())
path_to_chrome_instances = path + r'\instances_of_chrome'


def remove_all_existing_instances():
    all_instances = os.listdir(path_to_chrome_instances)
    if len(all_instances) != 0:
        for file in all_instances:
            try:
                os.remove(path=path_to_chrome_instances + '\\' + str(file))
            except:
                try:
                    shutil.rmtree(path_to_chrome_instances + '\\' + str(file))
                except:
                    print(traceback.print_exc())
                    time.sleep(10)


def start_chrome(port):
    driver = None
    try:
        command = fr'start chrome.exe --remote-debugging-port={port} --user-data-dir={path_to_chrome_instances}' \
                  + fr'\{port}'
        print('Creating directory')
        new_directory = path_to_chrome_instances + fr'\{port}'
        print(new_directory)
        os.mkdir(new_directory)
        print(command)
        os.system(command)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    except:
        print(traceback.print_exc())
    finally:
        if driver is not None:
            return driver


def start_chrome_and_retrieve_windows(port):
    driver = None
    pygetwindow_previous_windows = bwh.get_previous_pygetwindow_windows("Chrome")
    try:
        command = fr'start chrome.exe --remote-debugging-port={port} --user-data-dir={path_to_chrome_instances}' \
                  + fr'\{port}'
        print('Creating directory')
        new_directory = path_to_chrome_instances + fr'\{port}'
        print(new_directory)
        os.mkdir(new_directory)
        print(command)
        os.system(command)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    except:
        print(traceback.print_exc())
    finally:
        if driver is not None:
            # Retrieve windows
            pyget_chrome_window = bwh.get_new_pygetwindow_window("Chrome", pygetwindow_previous_windows)
            driver_parent_guid = bwh.get_selenium_driver_window_parent_guid(driver)
            chrome_data_dict = {
                    "driver": driver,
                    "pyget_chrome_window": pyget_chrome_window,
                    "driver_parent_guid": driver_parent_guid
                }
            print(f'Created chrome instance with following data: \n'
                  f'[ driver: {driver} ], '
                  f'[ pyget_chrome_window: {pyget_chrome_window} ], '
                  f'[ driver_parent_guid: {driver_parent_guid} ]')
            return chrome_data_dict
