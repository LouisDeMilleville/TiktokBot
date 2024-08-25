import config
import functions as fct
from nav import Navigator
from discord_webhook import DiscordWebhook
import time
import os
from selenium.webdriver.common.by import By
import random

#Loading the accounts from the cookies folder
accounts = []

def main():
    #Begin by loading all the accounts in the folder
    for filename in os.listdir('accounts_cookies'):
        if filename != "README.txt":
            file_path = os.path.join('accounts_cookies', filename)
            accounts.append(file_path)
            
    welcome_screen = """
  _________________  ____  ____    ____  _________________       _____     ____    ____              _____          _____   _________________ \n/                 \\|    ||    |  |    |/                 \\ ____|\\    \\   |    |  |    |        ___|\\     \\    ____|\\    \\ /                 \\\n\\______     ______/|    ||    |  |    |\\______     ______//     /\\    \\  |    |  |    |       |    |\\     \\  /     /\\    \\\\______     ______/\n   \\( /    /  )/   |    ||    | /    //   \\( /    /  )/  /     /  \\    \\ |    | /    //       |    | |     |/     /  \\    \\  \\( /    /  )/   \n    ' |   |   '    |    ||    |/ _ _//     ' |   |   '  |     |    |    ||    |/ _ _//        |    | /_ _ /|     |    |    |  ' |   |   '    \n      |   |        |    ||    |\\    \\'       |   |      |     |    |    ||    |\\    \\'        |    |\\    \\ |     |    |    |    |   |        \n     /   //        |    ||    | \\    \\      /   //      |\\     \\  /    /||    | \\    \\        |    | |    ||\\     \\  /    /|   /   //        \n    /___//         |____||____|  \\____\\    /___//       | \\_____\\/____/ ||____|  \\____\\       |____|/____/|| \\_____\\/____/ |  /___//         \n   |`   |          |    ||    |   |    |  |`   |         \\ |    ||    | /|    |   |    |      |    /     || \\ |    ||    | / |`   |          \n   |____|          |____||____|   |____|  |____|          \\|____||____|/ |____|   |____|      |____|_____|/  \\|____||____|/  |____|          \n     \\(              \\(    \\(       )/      \\(               \\(    )/      \\(       )/          \\(    )/        \\(    )/       \\(            \n      '               '     '       '        '                '    '        '       '            '    '          '    '         '            \n
    By https://github.com/LouisDeMilleville \n
    """
    print(welcome_screen)
    print("Accounts loaded : ", end=str(len(accounts))+"\n")
    print("Starting the bot...")
    while True:
        #Then it will follow 15 random accounts from the followers of the accounts put in the config file
        for account in accounts:
            #Generates a random user agent to use with this account to avoid detection by TikTok
            uagent = fct.getRandomUserAgent()
            #Creates a chromium instance with the user agent and loads the cookies of the account
            instance = Navigator(account, uagent)
            instance.startDriver()
            instance.loadCookies()
            driver = instance.getDriver()
            #Loads the profile of the account
            driver.get("https://www.tiktok.com/profile")
            fct.wait_for_page_load(driver)
            followers_element = driver.find_element(By.XPATH, "//strong[@data-e2e='followers-count']")
            followers_text = followers_element.text
            following_element = driver.find_element(By.XPATH, "//strong[@data-e2e='following-count']")
            following_text = following_element.text
            pseudo = fct.extract_text(driver.current_url)
            driver.get("https://www.tiktok.com/" + str(pseudo))
            #Displays basic informations on the terminal about the account currently used
            print(f"Username:{pseudo}\nFollowers:{followers_text}\nFollowing:{following_text}")
            i = 0
            fails = 0
            #Then it wil: follow 15 accounts from the followers of an account randomly selected from the wanted accounts
            while i < 15:
                fails = fails + fct.followUser(driver, random.choice(config.accounts_list))
                i = i+1
                #If it fails to follow more than 5 times, the account is skipped
                if fails > 5:
                    break
            #Then we collect refreshed data about the account
            driver.get("https://www.tiktok.com/" + str(pseudo))
            fct.wait_for_page_load(driver)
            followers_element = driver.find_element(By.XPATH, "//strong[@data-e2e='followers-count']")
            followers_text = followers_element.text
            following_element = driver.find_element(By.XPATH, "//strong[@data-e2e='following-count']")
            following_text = following_element.text
            #And we send this data to our Discord server
            webhook = DiscordWebhook(url=config.URL_WEBHOOK, content='Account: ' + str(pseudo) + ':\nFollowers : ' + str(followers_text) + '\nFollowing : ' + str(following_text))
            response = webhook.execute()
            #Finally, we close the chromium instance to save ressources
            instance.prepareClose(driver)
            driver.quit()
        #The bot can manage accounts without waiting if there are 18 or more. We add waiting time if there's less
        if len(accounts) < 18:
            pause_time = 200 * (18 - len(accounts))
            print("Sleeping for :", end=str(pause_time))
            time.sleep(pause_time)
            
try:
    main()
except Exception as e:
    print(e)
    main()
