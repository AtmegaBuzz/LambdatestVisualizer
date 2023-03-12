from selenium import webdriver
import chromedriver_autoinstaller
import json

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep

chromedriver_autoinstaller.install()

LOADING_SLEEP= 10


def process_browser_log_entry(entry):
    response = json.loads(entry['message'])['message']
    return response

options = Options()
options.add_argument("--start-maximized")


caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(options=options,desired_capabilities=caps)
driver.implicitly_wait(0.5)
driver.get("https://www.lambdatest.com/")


# navbar links
site_routes = [
    "https://www.lambdatest.com/",
    "https://www.lambdatest.com/enterprise",
    "https://www.lambdatest.com/pricing"
]

for a_tags in driver.find_elements(By.CLASS_NAME,"header_inner"):
    
    for href in a_tags.find_elements(By.TAG_NAME,"a"):
        site_routes.append(href.get_attribute("href"))


for link in site_routes:

    driver.get(link)
    # wait till the site is loaded
    WebDriverWait(driver,LOADING_SLEEP).until(EC.presence_of_element_located((By.TAG_NAME,"body")))


    browser_log = driver.get_log('performance') 
    events = [process_browser_log_entry(entry) for entry in browser_log]
    events = [event for event in events if 'Network.response' in event['method']]

    for packet in events:

        if "response" not in packet["params"]:
            continue

        print(packet["params"]["response"]["mimeType"])
        packet["params"]["response"]["status"]
        packet["params"]["response"]["url"]
        packet["params"]["response"]["securityState"]
        packet["params"]["response"]["responseTime"]
        packet["params"]["response"]["protocol"]
        packet["params"]["type"]
        
        




driver.quit()