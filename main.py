import requests, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from termcolor import cprint
import pyperclip

extension_code = 'mdaailjaighpfancjlladfeacpklnmef'


def add_network(driver, name_network):
    try:
        networks = {
            'Optimism': {
                'net_name': 'Optimism',
                'rpc': 'https://mainnet.optimism.io',
                'chain_id': 10,
                'symbol': 'ETH',
                'explorer': 'https://optimistic.etherscan.io/',
            },

            'Arbitrum': {
                'net_name': 'Arbitrum One',
                'rpc': 'https://arb1.arbitrum.io/rpc',
                'chain_id': 42161,
                'symbol': 'ETH',
                'explorer': 'https://arbiscan.io/',
            },

            'BSC': {
                'net_name': 'Smart Chain',
                'rpc': 'https://bsc-dataseed.binance.org/',
                'chain_id': 56,
                'symbol': 'BNB',
                'explorer': 'https://bscscan.com',
            },

            'Polygon': {
                'net_name': 'Polygon',
                'rpc': 'https://polygon-rpc.com',
                'chain_id': 137,
                'symbol': 'MATIC',
                'explorer': 'https://polygonscan.com/',
            },
            'Fantom': {
                'net_name': 'Fantom Opera',
                'rpc': 'https://fantom-mainnet.public.blastapi.io	',
                'chain_id': 250,
                'symbol': 'FTM',
                'explorer': 'https://ftmscan.com'
            },
            'Harmony': {
                'net_name': 'Harmony',
                'rpc': 'https://api.harmony.one',
                'chain_id': 1666600000,
                'symbol': 'ONE',
                'explorer': 'https://explorer.harmony.one'
            },
        }


        driver.get(f'chrome-extension://{extension_code}/home.html#settings/networks/add-network')

        try:
            got_it_x_path = '//*[@id="popover-content"]/div/div/section/div[3]/button'
            wait_elem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, got_it_x_path)))
            driver.find_element(By.XPATH, got_it_x_path).click()
        except:
            pass

        network_name_x_path = '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input'
        wait_elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, network_name_x_path)))
        network_name = driver.find_element(By.XPATH, network_name_x_path).send_keys(networks[name_network]['net_name'])
        network_name = driver.find_element(By.XPATH, network_name_x_path).click()

        new_rpc_x_path = '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input'
        new_rpc = driver.find_element(By.XPATH, new_rpc_x_path).send_keys(networks[name_network]['rpc'])
        new_rpc = driver.find_element(By.XPATH, new_rpc_x_path).click()

        chain_x_path = '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input'
        chain = driver.find_element(By.XPATH, chain_x_path).send_keys(networks[name_network]['chain_id'])
        chain = driver.find_element(By.XPATH, chain_x_path).click()

        currency_symbol_x_path = '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input'
        currency_symbol = driver.find_element(By.XPATH, currency_symbol_x_path).send_keys(
            networks[name_network]['symbol'])
        currency_symbol = driver.find_element(By.XPATH, currency_symbol_x_path).click()

        explorer_url_x_path = '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/label/input'
        explorer_url = driver.find_element(By.XPATH, explorer_url_x_path).send_keys(networks[name_network]['explorer'])
        explorer_url = driver.find_element(By.XPATH, explorer_url_x_path).click()

        time.sleep(1)
        new_rpc = driver.find_element(By.XPATH, new_rpc_x_path).click()
        chain = driver.find_element(By.XPATH, chain_x_path).click()
        currency_symbol = driver.find_element(By.XPATH, currency_symbol_x_path).click()
        time.sleep(1)

        try:
            save_button_x_path = '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]'
            wait_elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, save_button_x_path)))
            save = driver.find_element(By.XPATH, save_button_x_path).click()
        except:
            print("There was a problem with adding " + networks[name_network]['net_name'])

        try:
            got_it_x_path = '//*[@id="popover-content"]/div/div/section/div[3]/button'
            wait_elem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, got_it_x_path)))
            driver.find_element(By.XPATH, got_it_x_path).click()
        except:
            pass

        time.sleep(1)
    except:
        cprint(f'network < {name_network} > is already add', 'white')


def main(zero, ads_id, seed, password):
    try:
        # working with ads brow
        open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id
        close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id
        resp = requests.get(open_url).json()
        chrome_driver = resp["data"]["webdriver"]
        chrome_options = Options()
        service = Service(executable_path=chrome_driver)
        chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        driver = webdriver.Chrome(service=service, options=chrome_options)
        # ads browser has been opened
        url = f'chrome-extension://{extension_code}/home.html'
        driver.get(url)
        time.sleep(15)
        # Goes to the main page
        try:
            wait_elem = WebDriverWait(driver, 4).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[2]/button')))
        except:
            if driver.current_url != url:
                driver.get(url)

        try:
            import_wallet_x_path = '//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[2]/button'
            wait_elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, import_wallet_x_path)))
            driver.find_element(By.XPATH, import_wallet_x_path).click()

            agree_x_path = '//*[@id="app-content"]/div/div[2]/div/div/div/div/button[1]'
            wait_elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, agree_x_path)))
            agree = driver.find_element(By.XPATH, agree_x_path).click()

            words = seed.split()
            for x in range(12):
                phrase_x_path = f'//*[@id="import-srp__srp-word-{x}"]'
                wait_elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, phrase_x_path)))
                # insert a word from phrase
                driver.find_element(By.XPATH, phrase_x_path).send_keys(words[x])
                driver.find_element(By.XPATH, phrase_x_path).click();
                print(x, words[x])

            confirm_x_path = '//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/button'
            time.sleep(2)
            driver.find_element(By.XPATH, confirm_x_path).click()
            time.sleep(2)

            password_x_path = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input'
            new_password = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, password_x_path)))
            driver.find_element(By.XPATH, password_x_path).send_keys(password)
            driver.find_element(By.XPATH, password_x_path).click()

            password_conf_x_path = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input'
            driver.find_element(By.XPATH, password_conf_x_path).send_keys(password);
            driver.find_element(By.XPATH, password_conf_x_path).click()

            agree_terms_x_path = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input'
            driver.find_element(By.XPATH, agree_terms_x_path).click()
            time.sleep(1)
            import_button_x_path = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button'
            driver.find_element(By.XPATH, import_button_x_path).click()

            got_it_x_path = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'
            WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, got_it_x_path)))
            driver.find_element(By.XPATH, got_it_x_path).click()
        except Exception as i:
            print('Seems like phrase was added before, trying to login.')

        #Let's login to the wallet
        url = f'chrome-extension://{extension_code}/home.html#unlock'
        driver.get(url)

        pass_input_x_path = '//*[@id="password"]'
        wait_elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, pass_input_x_path)))
        driver.find_element(By.XPATH, pass_input_x_path).send_keys(password);
        driver.find_element(By.XPATH, pass_input_x_path).click()
        time.sleep(1)
        # There are some additional windows with confirmation that could occur. We need to proceed them.
        try:
            unlock_wallet_x_path = '//*[@id="app-content"]/div/div[2]/div/div/div/div/button'
            wait_elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, unlock_wallet_x_path)))
            driver.find_element(By.XPATH, unlock_wallet_x_path).click()
        except:
            unlock_wallet_x_path = '//*[@id="app-content"]/div/div[3]/div/div/button'
            wait_elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, unlock_wallet_x_path)))
            driver.find_element(By.XPATH, unlock_wallet_x_path).click()

        try:
            got_it_x_path = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'
            wait_elem = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, got_it_x_path)))
            driver.find_element(By.XPATH, got_it_x_path).click()

            next_x_path = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'
            wait_elem = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, next_x_path)))
            driver.find_element(By.XPATH, next_x_path).click()

            ready_x_path = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'
            wait_elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ready_x_path)))
            driver.find_element(By.XPATH, ready_x_path).click()

        except:
            pass

        try:
            got_it_x_path = '//*[@id="popover-content"]/div/div/section/div[3]/button'
            wait_elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, got_it_x_path)))
            driver.find_element(By.XPATH, got_it_x_path).click()
        except:
            pass

        try:
            protect_funds_got_it_x_path = '//*[@id="popover-content"]/div[2]/div/section/div[2]/div/div[2]/div/button'
            wait_elem = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, protect_funds_got_it_x_path)))
            driver.find_element(By.XPATH, protect_funds_got_it_x_path).click()
        except:
            pass

        print("Successfully logged in, starting adding networks")
        # =================================== if you don't need to add a networks, delete everything below ===================================
        add_network(driver, 'BSC')
        add_network(driver, 'Polygon')
        add_network(driver, 'Optimism')
        add_network(driver, 'Arbitrum')
        add_network(driver, 'Harmony')
        add_network(driver, 'Fantom')
        # ===================================================================================================================================
        print("Finishing adding networks")

        #quit.
        driver.quit()
        requests.get(close_url)

        cprint(f'{zero + 1}. {ads_id} = done', 'green')

    except Exception as ex:
        cprint(f'{zero + 1}. {ads_id} = already done, or some problem occured.', 'yellow')
        driver.quit()
        requests.get(close_url)


with open("id_users.txt", "r") as f:
    id_users = [row.strip() for row in f]

with open("seeds.txt", "r") as f:
    seeds = [row.strip() for row in f]

zero = -1
for ads_id in id_users:
    zero = zero + 1
    seed = seeds[zero]
    password = ''  # password for metamask

    main(zero, ads_id, seed, password)
