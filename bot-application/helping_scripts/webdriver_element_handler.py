from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@staticmethod
def retrieve_element_by_xpath(driver, xpath):
    return WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, xpath)))


@staticmethod
def retrieve_element_by_id(driver, id):
    return WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, id)))


@staticmethod
def retrieve_element_by_class_name(driver, class_name):
    return WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, class_name)))

