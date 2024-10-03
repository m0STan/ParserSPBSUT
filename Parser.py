from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver import DesiredCapabilities

from selenium.webdriver.chrome.service import Service as ChromeService
from dotenv import load_dotenv
import os
load_dotenv()

username = "shnyrok2002@gmail.com"
password = "alesha2002"


options = Options()
options.set_capability("acceptInsecureCerts",True)
options.add_argument("--no-sandbox")
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options, )

driver.minimize_window()
driver.set_window_position(-2000, 0)



driver.get("https://lk.sut.ru/cabinet/?login=no")
driver.implicitly_wait(0.5)

# find username/email field and send the username itself to the input field
driver.find_element("id", "users").send_keys(username)
# find password input field and insert password as well
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

ls1 = []
if elements[1:]:
    for e in elements[1:]:
        print(e.text)
        if e.get_attribute('id'):
            ls1.append(e.get_attribute('id')[4:])
    print(ls1)

    driver.implicitly_wait(0.5)

    try:
        driver.get("https://lk.sut.ru/cabinet/?login=yes")

        driver.implicitly_wait(0.5)

        driver.find_element(By.CSS_SELECTOR,"#heading1 > h5 > div").click()

        driver.implicitly_wait(0.5)

        driver.find_element(By.CSS_SELECTOR,'#menu_li_6118').click()
    except:
        print(".Click Exception")
    if len(ls1):
        for i in ls1:
            s = '#knop'
            s+=i
            s+=' > a'
            # print(s)
            try:
                element = driver.find_element(By.CSS_SELECTOR, s)
                element.click()
                # element.click()
            except:
                print("Занятие еще не началось или отсутствует")
    driver.get("https://lk.sut.ru/cabinet/project/cabinet/forms/raspisanie.php")

    elements = driver.find_elements(By.TAG_NAME,'span')
    print("Проверка")
    for i in elements[1:]:
        print(i.text)
driver.close()

