# IMPORTS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Uses selenium chrome driver

def retrieve_element_by_xpath(driver, xpath):
    return WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, xpath)))


def retrieve_element_by_id(driver, id):
    return WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, id)))


def retrieve_element_by_class_name(driver, class_name):
    return WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
