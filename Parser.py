from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from dotenv import load_dotenv
import os
import time

load_dotenv()
username = os.environ.get("USER")
password = os.environ.get("PASS")

def init_driver()-> webdriver.Chrome:

    options = Options()
    options.set_capability("acceptInsecureCerts",True)
    options.add_argument("--no-sandbox")
    options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    options.add_argument("--headless")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options, )
    driver.minimize_window()
    driver.set_window_position(-2000, 0)
    return driver

def start_lessons(driver: webdriver.Chrome):
    while True:
        driver.get("https://lk.sut.ru/cabinet/?login=no")
        driver.implicitly_wait(0.5)

        driver.find_element("id", "users").send_keys(username)
        driver.find_element("id", "parole").send_keys(password)

        # click login button
        driver.find_element("id", "logButton").click()
        driver.implicitly_wait(0.5)
        WebDriverWait(driver=driver, timeout=10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )

        driver.get("https://lk.sut.ru/cabinet/?login=yes")
        driver.implicitly_wait(0.5)


        driver.get("https://lk.sut.ru/cabinet/project/cabinet/forms/raspisanie.php")

        elements = driver.find_elements(By.TAG_NAME,'span')
        driver.implicitly_wait(0.5)

        lessons = []
        if elements[1:]:
            for e in elements[1:]:
                print(e.text)
                if e.get_attribute('id'):
                    lessons.append(e.get_attribute('id')[4:])
            print(lessons)

            driver.implicitly_wait(0.5)

            try:
                driver.get("https://lk.sut.ru/cabinet/?login=yes")

                driver.implicitly_wait(0.5)

                driver.find_element(By.CSS_SELECTOR,"#heading1 > h5 > div").click()

                driver.implicitly_wait(0.5)

                driver.find_element(By.CSS_SELECTOR,'#menu_li_6118').click()
            except:
                print(".Click Exception")

            if len(lessons):
                for i in lessons:
                    s = '#knop'
                    s+=i
                    s+=' > a'
                    # print(s)
                    try:
                        element = driver.find_element(By.CSS_SELECTOR, s)
                        element.click()
                    except:
                        print("Занятие еще не началось или отсутствует")
            
        driver.get("https://lk.sut.ru/cabinet/project/cabinet/forms/raspisanie.php")

        elements = driver.find_elements(By.TAG_NAME,'span')
        print("Проверка")
        for i in elements[1:]:
            print(i.text)
        time.sleep(10)
        print("checking")
        # driver.close()

if __name__=="__main__":
    driver = init_driver()
    start_lessons(driver)

