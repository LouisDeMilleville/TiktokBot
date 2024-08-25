import random
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import subprocess
import config
import time

#Returns a random user agent
def getRandomUserAgent():
    return random.choice(config.user_agents)

#Extract the usernam from the url
def extract_text(url):
    match = re.search(r'\.com/(.*?)\?', url)
    if match:
        return match.group(1)
    else:
        return None

#Wait until the page is loaded        
def wait_for_page_load(driver, timeout=60):
    try:
        element_present = EC.presence_of_element_located((By.TAG_NAME, 'body'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Took too much time to load.")
 
#Follow a user from the followers of the account specified in the url       
def followUser(driver, url):
    try:
        driver.get(url)
        wait_for_page_load(driver)
        if config.lang == "fr":
            script_btn_follow = 'document.evaluate("//*[text()=\'Abonnés\']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();'
        if config.lang == "en":
            script_btn_follow = 'document.evaluate("//*[text()=\'Followers\']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();'
        if config.lang == "es":
            script_btn_follow = 'document.evaluate("//*[text()=\'Seguidores\']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();'
        if config.lang == "de":
            script_btn_follow = 'document.evaluate("//*[text()=\'Follower\']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();'
        if config.lang == "ar":
            script_btn_follow = 'document.evaluate("//*[text()=\'متابعون\']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();'
        if config.lang == "zh":
            script_btn_follow = 'document.evaluate("//*[text()=\'粉絲\']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();'
        if config.lang == "hi":
            script_btn_follow = 'document.evaluate("//*[text()=\'फॉलोअर\']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();'
        if config.lang == "bn":
            script_btn_follow = 'document.evaluate("//*[text()=\'অনুসরণকারীরা\']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();'
        if config.lang == "pt":
            script_btn_follow = 'document.evaluate("//*[text()=\'Seguidores\']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();'
        driver.execute_script(script_btn_follow)
        time.sleep(3)
        if config.lang == "fr":
            btn_test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'Suivre') and text()='Suivre'][1]")))
        if config.lang == "en":
            btn_test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'Follow') and text()='Follow'][1]")))
        if config.lang == "es":
            btn_test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'Seguir') and text()='Seguir'][1]")))
        if config.lang == "de":
            btn_test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'Folgen') and text()='Folgen'][1]")))
        if config.lang == "ar":
            btn_test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'متابعة') and text()='متابعة'][1]")))
        if config.lang == "zh":
            btn_test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, '關注') and text()='關注'][1]")))
        if config.lang == "hi":
            btn_test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'फ़ॉलो करें') and text()='फ़ॉलो करें'][1]")))
        if config.lang == "bn":
            btn_test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'অনুসরণ করুন') and text()='অনুসরণ করুন'][1]")))
        if config.lang == "pt":
            btn_test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'Seguir') and text()='Seguir'][1]")))
        btn_test.click()
        time.sleep(5)
        return 0
    except Exception as e:
        print("An error has occured, trying again...")
        time.sleep(5)
        return 1
