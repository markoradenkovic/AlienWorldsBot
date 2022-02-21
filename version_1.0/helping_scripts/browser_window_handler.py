# IMPORTS
import pygetwindow


def get_new_browser_window(search_string, previous_windows):
    new_browser_window = None
    current_browser_windows = pygetwindow.getWindowsWithTitle(title=search_string)
    for window in current_browser_windows:
        if window not in previous_windows:
            new_browser_window = window
    print("New Browser Window Found: " + str(new_browser_window))
    return new_browser_window


def get_new_selenium_driver_window_guid(driver, previous_windows):
    current_windows = driver.window_handles
    for guid in current_windows:
        if guid not in previous_windows:
            return guid  # return the new_window_detected


