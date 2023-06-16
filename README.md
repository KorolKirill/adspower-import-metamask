# adspower-import-metamask

Данный скрипт импортирует заранее созданные метамаски в твои готовые профили в [adspower](https://app.adspower.net/). <br/>
После импорта он добавляет сети optimism, bsc и arbitrum, harmony, fantom в кошелек. 

1. экспортируй ids из adspower со своих профилей.
2. добавляешь эти ids в файл id_users.txt
3. добавляешь сид фразы от заранее созданных кошельков в файл seeds.txt
4. меняешь в файле main.py переменную password
5. запускаешь файл main.py
1
не забудь заранее войти в свой [adspower](https://app.adspower.net/), скрипт работает именно через него. 

Работает только на метомаске до версии 25

библиотеки для скачивания : 
pip install selenium, requests, pyperclip, termcolor
