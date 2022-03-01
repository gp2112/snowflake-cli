from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from datetime import datetime
import requests
import time
import os
import sys
import asyncio

def logPeerIp(log: str) -> str:
    l = log.replace('\n', ' ').split()[10:]
    ip, port = None, None
    if 'IP6' in l:
        ip = l[l.index('IP6')+1].strip()

    elif 'IP4' in l:
        ip = l[l.index('IP4')+1].strip()

    return ip

def getPeerLocation(ip: str) -> dict:
    r = requests.get(f'http://ip-api.com/json/{ip}?fields=16393')
    if r.status_code != 200:
        return {}

    data = r.json()
    if data.get('status') != 'success':
        return {}

    return r.json()

def parsePeer(msg: str, save=True, get_loc=True):
    ip = logPeerIp(msg)
    p_loc = getPeerLocation(ip) if get_loc else {}

    print(f"{ip} from {p_loc.get('region')}-{p_loc.get('country')} is conected to you")
    if save:
        statsdb.savePeer(timestmp, ip, p_data.get('country'), p_data.get('region'))


async def main():

    save_data = '--no-persist' not in sys.argv #saves peer's data in database
    get_loc = '--no-location' not in sys.argv # check peer's location using ip-api.com

    if save_data: import statsdb

    started_time = time.time()

    print('Starting snowflake...')

    if save_data and not os.path.isfile(statsdb.db_name):
        print('Creating database...')
        statsdb.createDb()
        print(f'{statsdb.db_name} created!')

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

    peers_connected = 0

    while True:
        try:
            current_time = time.time()

            for entry in driver.get_log('browser'):
                timestmp = int(str(entry['timestamp'])[:-3])
                date = datetime.fromtimestamp(timestmp).strftime('%Y-%m-%d %H:%M:%S')
                msg = entry['message'].split('"')[1].replace('\\r\\n', f'\n{date}')

                print(f'{date} - {msg}')

                if 'IP4' in msg or 'IP6' in msg:
                    peers_connected += 1
                    # run parsePeer on another thread for ip location request and peer database store
                    await asyncio.to_thread(parsePeer, msg, save=save_data, get_loc=get_loc)

            # shows you each 10min how many people have conected with you
            if (current_time-started_time)%600==0:
                print(f'\nYou have helped {peers_connected} people :)\n')

        except KeyboardInterrupt:
            print('\rclosing...')
            time.sleep(3)
            driver.quit()
            break

    if peers_connected > 0:
        p = 'people' if peers_connected>1 else 'person'
        print(f'You have helped {peers_connected} {p}!')

if __name__ == '__main__':
    asyncio.run(main())
