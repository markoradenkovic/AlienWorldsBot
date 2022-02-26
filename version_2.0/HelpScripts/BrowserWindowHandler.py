# IMPORTS
import pygetwindow


# PYGETWINDOWS CODE
def get_previous_pygetwindow_windows(search_string):
    # Call this function before calling get_new_pygetwindow_window()
    return pygetwindow.getWindowsWithTitle(title=search_string)


def get_new_pygetwindow_window(search_string, previous_windows):
    current_browser_windows = pygetwindow.getWindowsWithTitle(title=search_string)
    for window in current_browser_windows:
        if window not in previous_windows:
            print(f'NEW PyGetWindow BROWSER WINDOW FOUND WITH TITLE \'{search_string}\': \n' + str(window)+"\n")
            return window


# SELENIUM CODE
def get_selenium_driver_window_parent_guid(driver):
    # Call this function directly after creating a new chrome instance
    return driver.current_window_handle


def get_previous_selenium_driver_windows_guid(driver):
    # Call this function before calling get_new_selenium_driver_window_guid()
    return driver.window_handles


def get_new_selenium_driver_window_guid(driver, previous_windows):
    current_windows = driver.window_handles
    for guid in current_windows:
        if guid not in previous_windows:
            print(f'NEW SELENIUM DRIVER WINDOW FOUND WITH GUID: \n' + str(guid)+"\n")
            return guid  # return the new window's guid
