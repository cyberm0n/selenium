import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle



if __name__ == '__main__':
    



    options = webdriver.ChromeOptions()
    #options.add_argument('proxy-server=106.122.8.54:3128')
    options.add_argument(r'--user-data-dir=C:\\Users\\sefa\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    options.add_argument('--load-extension=C:\\Users\\sefa\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\mpbjkejclgfgadiemmefgebjfooflfhl\\1.3.2_0')
    options.add_argument('--headless')
    browser = uc.Chrome(
        options=options,
    )
    start = time.time()
    browser.get('https://www.spy.gen.tr/')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
        print(cookie)

    browser.refresh()
    end = time.time()
    print(end - start)
    time.sleep(400)
