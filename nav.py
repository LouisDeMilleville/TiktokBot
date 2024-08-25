from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import json
import time

#A class used to manage an instance of chromium
class Navigator:
    
    path_cookies: str
    agent: str
    driver: webdriver


    def __init__(self, path_cookies, agent):
        self.path_cookies = path_cookies
        self.agent = agent
    
    
    def startDriver(self):
        options = ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--profile-directory=Default')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--lang=en")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=720,1080")
        options.add_experimental_option("prefs", {"navigator.platformOverride": "Linux armv8l"})
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        
        arg_user_agent = "--user-agent=" + str(self.agent)
        options.add_argument(arg_user_agent)

        self.driver = webdriver.Chrome(options=options)
        
    def loadCookies(self):
        self.driver.get('https://www.tiktok.com/login')
        time.sleep(5)
        with open(self.path_cookies, 'r') as cookiesfile:
            cookies = json.load(cookiesfile)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
            
    def getDriver(self):
        return self.driver
        
    def prepareClose(self, driver):
        self.driver = driver
            
    def closeDriver(self):
        self.driver.quit()
    
        
        
    
