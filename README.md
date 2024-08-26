# What's this Tiktok Bot ?
(French below)

This Tiktok bot allows you to grow your Tiktok accounts followers on the communities you want by following followers of major accounts from the communities you want to get followers from. It also send updates to your Discord server while it's running using webhooks.

# How does it works ?
Before starting the bot, you choose target accounts from a community that will be used to target accounts related to this community. The bot will then follow 15 random users every hour (not more to avoid detection) from the recent followers of the accounts you choose before, and it can manage multiple accounts at the same time.
By using it, your account will be following a lot of people interested by these communities (A user rarely follows an account related to a community he hates), then some of them will follow you back. Finally, your accounts will get many real followers interested in the communities you chosed, making it easier to get a lot of traffic and engagement on videos posted on this account in the future.

# How can i use it ?
⚠️ This bot has been developped and tested on Linux (Ubuntu 22.04 & 24.04). It should work on Windows and other systems since it uses Python and Chromium, but you may have to do some adjustements ⚠️

You will need python and pip first, if it's not already installed.

Then install chromium and chromedriver
> sudo apt-get install chromium

and
> sudo apt-get install chromium-chromedriver

Now clone this repo and move to it's folder, then create a virtual environnement and activate it.
> virtualenv venv
> 
> source venv/bin/activate

Now install the requirements inside your virtual environnement
> pip3 install -r requirements.txt

Now you will need to create the cookies to allow the bot to use your accounts, follow the tutorial in the README file in the accounts_cookies folder.

You're almost ready to start, don't forget to edit the config.py file before starting it. Here are the settings to change:
- lang: If your Chromium isn't in English, change the code to match your language
- URL_WEBHOOK: Create a webhook on your Discord server and paste the url here (Mandatory to work, or you will have to remove the lines related to DiscordWebhook in the code if you don't want to use it).
- accounts_list: Place the url of the accounts you want to get followers from. You can put as many accounts as you want since one of them will be picked randomly each time the bot will try to follow a user

Now you can start the bot, run it at least one time with chromium visible to make sure it works on your side
> python3 main.py

# How to run it on the background
Once you verified everything works perfectly, you can run it on the background to avoid rendering chromium and save ressources.

Install xvfb to be able to run a headless chromium without the headless mode (Tiktok can detect that you're using a headless browser and block the follow tries so we use this to avoid being detected).
> sudo apt-get install xvfb

Now you can run it in the background. Just open a terminal and move to the bot's folder, then type this.
> source venv/bin/activate && xvfb-run -a -s "-screen 0 1080x720x24" python3 main.py &

You can now close the terminal. The bot is now running fully in the background and you will get updates from it from your Discord webhook

==========================================================================================================================================================
# Qu'est-ce que ce bot Tiktok ?

Ce bot Tiktok vous permet de faire grossir le nombre d'abonnés de vos comptes sur les communautées que vous souhaitez en suivant massivement les abonnés de comptes réputés dans les communautées parmis lesquelles vous souhaitez obtenir des abonnés. Il vous transmet également des information pendant qu'il est en fonctionnement via un webhook Discord.

# Comment ça marche ?
Avant de démarrer le bot, vous devrez sélectionner des comptes issus de communautées qui seront utilisés pour cibler les comptes à suivre. Le bot va ensuite suivre 15 personnes aléatoires par heure (pas plus pour éviter d'être détecté comme un bot) parmis les abonnés récents des comptes que vous avez sélectionné précédemment. Il est capable de gérer plusieurs comptes Tiktok en simultané.
En utilisant ce bot, votre compte va suivre un grand nombre de personnes intéressées par ces communautées (Un utilisateur suit rarement un compte traitant d'une communautée qu'il déteste), et un certain nombre d'entre eux vont vous suivre en retour. Au final, vos comptes vont obtenir beaucoup d'abonnés issus des communautées que vous avez choisies, ce qui rendra beaucoup plus simple le fait d'obtenir beaucoup de traffic et d'engagement sur les vidéos postées sur ce compte dans le futur.

# Comment l'utiliser ?
⚠️ Ce bot a été développé et testé sur Linux (Ubuntu 22.04 & 24.04). Il devrait fonctionner sur Windows et d'autres systèmes étant donné qu'il utilisé Python et Chromium, mais vous aurez peut-être à effectuer quelques ajustements ⚠️

Vous aurez besoin de python et pip, s'ils ne sont pas déjà installés.

Ensuite, installez chromium et chromedriver
> sudo apt-get install chromium

et
> sudo apt-get install chromium-chromedriver

Maintenant clonez ce dépot, ouvrez un terminal et déplacez vous dans le dossier du bot, puis créez un environnement virtuel et activez le.
> virtualenv venv
> 
> source venv/bin/activate

Installez les prérequis dans votre environnement virtuel
> pip3 install -r requirements.txt

Maintenant vous allez avoir besoin de créer les cookies pour vos comptes, suivez le tutoriel dans le fichier README.txt du dossier accounts_cookies.

Vous êtes pratiquement prêt à lancer le bot, n'oubliez pas d'éditer le fichier config.py avant de le démarrer. Voici les paramètres à changer:
- lang: Si votre chromium n'est pas en Anglais, changez le code par celui correspondant à votre langue
- URL_WEBHOOK: Créez un webhook sur votre serveur Discord et collez-le ici (Obligatoire pour que le bot fonctionne tel quel, ou bien vous allez devoir effacer toutes les lignes relatives à DiscordWebhook dans le code si vous ne souhaitez pas l'utiliser).
- accounts_list: Placez les liens des comptes desquels vous souhaitez obtenir des abonnés. Vous pouvez en mettre autant que vous voulez étant donné que l'un d'entre eux sera tiré au sort aléatoirement à chaque fois que le bot voudra suivre un compte.

Vous pouvez désormais démarrer le bot, lancez le au moins une fois avec chromium visible pour vous assurer que tout fonctionne correctement de votre coté
> python3 main.py

# Comment le lancer en arrière plan ?
Une fois que vous avez vérifié que tout fonctionne parfaitement, vous pouvez le lancer en arrière plan afin d'éviter d'afficher les fenêtres de chromium et ainsi économiser des ressources.

Installez xvfb pour pouvoir lancer chromium sans affichage sans avoir à utiliser le mode headless (Tiktok peut détecter que vous utilisez un navigateur headless et bloquer les tentatives de follow donc on utilise cela pour éviter d'être détecté).
> sudo apt-get install xvfb

Vous pouvez désormais le lancer en arrière plan. Ouvrez simplement un terminal et déplacez vous dans le répertoire du bot, puis tapez ceci:
> source venv/bin/activate && xvfb-run -a -s "-screen 0 1080x720x24" python3 main.py &

Vous pouvez désormais fermer le terminal. Le bot fonctionne désormais totalement en arrière plan, et vous aurez régulièrement de ses nouvelles via le webhook Discord
