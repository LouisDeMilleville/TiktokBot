import random

#Language of your chromium instance
lang = "en" #english: en   french: fr  spanish: es  german: de  arabic: ar  chinese: zh  hindi: hi  bengali: bn  portuguese: pt


#If your current language is not supported, just switch it to english

#Discord Webhook URL to send informations to your Discord server while the bot is running
URL_WEBHOOK = 'PUT_YOUR_DISCORD_WEBHOOK_URL_HERE'

#Accounts to follow users from
accounts_list = ['https://www.tiktok.com/@account1', 'https://www.tiktok.com/@account2', 'https://www.tiktok.com/@account3']

#User agents list which is used by the bot, not necessary to change
user_agents = [
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; P30 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; LM-G820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Mi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Xperia 1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Moto G7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; ASUS_Z01QD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Nokia 9 PureView) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Galaxy A50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; ONEPLUS A6013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; CPH1907) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; ELE-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; LM-V405) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Mi MIX 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; I3311) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Nokia 8.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Mi A3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Galaxy S9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; ONEPLUS A6010) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; CPH2005) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Pixel 3a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; ELS-NX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; H8416) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Mi 9T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; D6603) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; XT1965-6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; I8190) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; PAFM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; ONEPLUS A6010) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Find X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; Pixel 3a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; LM-G710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; EML-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; RMX1921) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4324.150 Mobile Safari/537.36",
]
