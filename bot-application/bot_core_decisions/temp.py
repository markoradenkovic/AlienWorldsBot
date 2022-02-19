import pygetwindow
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from helping_scripts import executing_chrome

# Läs in 1 konto från JSON
# Create list for storing selenium chrome instances
selenium_chrome_instances = []

executing_chrome.remove_all_existing_instances()
# Later on, loop through the account list and start 1 chrome for each account
# Can use ports from 8001+
# Öppna 1 Chrome Instans
chrome1 = executing_chrome.start_chrome(8001, 'fakewalletaddress')

# Identify Browser ID
# print( pygetwindow.getAllWindows() )
# print( pygetwindow.getAllTitles() )

retrieved_chrome_ids = pygetwindow.getWindowsWithTitle('Chrome')
for retrieved_id in retrieved_chrome_ids :
    if retrieved_id not in chrome_window_ids:
        chrome_window_ids.append(retrieved_id)
print(chrome_window_ids)
chrome1.get(url='https://www.facebook.com')

object_to_find = WebDriverWait(chrome1, 100).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]')))
object_to_find.click()

# Få procesen att fungera
# Logga in
# Börja spela
# Under väntetiden, vänta tills GUI matchar att köra igen
# Om jag gör dåligt, kan alla chrome fönster vänta istället för jag just vill, anpassa koden
# Spela igen
# Repeat

# List, Tuple

list1 = [1, 2, 3, 4]
tuple1 = (1, 2, 3, 4)

print(list1)
list1_to_tuple = tuple(list1)
print(list1_to_tuple)

