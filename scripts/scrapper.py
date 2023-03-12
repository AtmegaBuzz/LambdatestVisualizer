import json
import chromedriver_autoinstaller

from uuid import uuid4
from elasticsearch import Elasticsearch

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestEngine:

    def __init__(
            self,
            initial_site_routes,
            chrome_options,
            capabilities,
            loading_sleep,
            es_url="http://localhost:9200",
            es_index="network_logs"
            ):

        self.es = Elasticsearch(es_url)
        self.es_index = es_index
        self.LOADING_SLEEP = loading_sleep
        self.options = chrome_options
        self.caps = capabilities
        self.site_routes = initial_site_routes
    

    def elastic_insert(self,body):
        self.es.index(
            index=self.es_index,
            id=uuid4(),
            body=body
        )

    @staticmethod
    def process_browser_log_entry(entry):
        response = json.loads(entry['message'])['message']
        return response


    def run(self):
        
        driver = webdriver.Chrome(
            options=self.options,
            desired_capabilities=self.caps
        )

        driver.implicitly_wait(0.5)
        driver.get(self.site_routes[0])

        # scrape href's present in the navbar
        for a_tags in driver.find_elements(By.CLASS_NAME,"header_inner"):
    
            for href in a_tags.find_elements(By.TAG_NAME,"a"):
                self.site_routes.append(href.get_attribute("href"))


        for link in site_routes:

            driver.get(link)

            # wait till the site is loaded
            WebDriverWait(driver,self.LOADING_SLEEP).until(EC.presence_of_element_located((By.TAG_NAME,"body")))

            # extract network logs 
            browser_log = driver.get_log('performance') 
            events = [TestEngine.process_browser_log_entry(entry) for entry in browser_log]
            events = [event for event in events if 'Network.response' in event['method']]

            for packet in events:

                if "response" not in packet["params"]:
                    continue

                self.elastic_insert(packet)
                

        driver.quit()




if __name__ == "__main__":


    chromedriver_autoinstaller.install()

    LOADING_SLEEP= 10


    options = Options()
    options.add_argument("--start-maximized")

    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}



    # navbar links
    site_routes = [
        "https://www.lambdatest.com/",
        "https://www.lambdatest.com/enterprise",
        "https://www.lambdatest.com/pricing"
    ]


    network_test = TestEngine(
        site_routes,
        options,
        caps,
        20
    )

    network_test.run()