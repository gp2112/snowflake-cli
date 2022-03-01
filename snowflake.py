from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from datetime import datetime
import time

print('Starting snowflake...')

options = Options()
options.add_argument('--headless')

d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = {'browser':'ALL'}

driver = webdriver.Chrome(options=options, desired_capabilities=d)
driver.get('https://snowflake.torproject.org/embed.html')

# try to click the button 10 times
for i in range(10):
    time.sleep(2)
    try:
        button = driver.find_element(by=By.CLASS_NAME, value='slider')
        button.click()
        print('connected!')
        break
    except ElementNotInteractableException:
        pass


while True:
    try:
        for entry in driver.get_log('browser'):
            date = datetime.fromtimestamp(int(str(entry['timestamp'])[:-3])).strftime('%Y-%m-%d %H:%M:%S')
            msg = entry['message'].split('"')[1].replace('\\r\\n', '\n')
            print(f'{date} - {msg}')

    except KeyboardInterrupt:
        print('closing...')
        button.click()
        time.sleep(3)
        driver.quit()
        break
