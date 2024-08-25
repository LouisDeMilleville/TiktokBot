HOW TO IMPORT YOUR TIKTOK ACCOUNTS
==================================
First, install chromium on your device
sudo apt-get install chromium && sudo apt-get install chromium-chromedriver

Then, install this extension to be able to export cookies easily in json
https://chromewebstore.google.com/detail/export-cookie-json-file-f/nmckokihipjgplolmcmjakknndddifde


Now, for EACH account you want to use with the bot, do this:
/!\ Disconnect from ALL the other browsers where this account is connected /!\ (You can stay connected in the app, this only applies to the browser version)
- Log into the account on chromium
- Accept all cookies
- Follow all the accounts you want to farm followers from on this account
- Go on the profile of the account
- Click on the extension and export the cookies
- Copy the generated json file in this folder (accounts_cookies) and rename it with the username of this account.json
- Now on chromium, right click + inspect element
- Click on the arrow on the side panel > application, then delete all the entries linked to tiktok in the categories local_storage, session_storage and cookies
- Now refresh the page. You should be disconnected from your account. If it's still connected, make sure that you have deleted all the required entries in the storage
- Do that for each account and keep the generated json files in the folder

/!\ Do not connect to any account used by the bot on the browser version, use the app only or it will make your cookies obsolete /!\
