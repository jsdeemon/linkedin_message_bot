## Original code taken ftom here: https://github.com/evilprince2009/linkedin-connector 

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By


mail = input("Enter your LinkedIn Email: ").strip()
key = input("Enter your LinkedIn Password: ").strip()
search_param = input("Enter search phrase to find users: ").strip()
message = input("Enter message text (maximum 300 chars): ").strip()
pages_upto = int(input("Enter maximum pages number in result: ").strip())
totalCount = int(input("Enter maximum of sending requests: ").strip())
maxDelay = int(input("Maximum delay (in seconds): ").strip())

url = "https://www.linkedin.com"
search_param = search_param.replace(" ", "%20")

browser_script = "arguments[0].click();"
## browser = webdriver.Edge("msedgedriver.exe")
browser = webdriver.Firefox()
browser.maximize_window()
browser.get(url)
time.sleep(random.randint(1, 5))

username = browser.find_element(By.XPATH, value="//input[@name='session_key']")
password = browser.find_element(By.XPATH, value="//input[@name='session_password']")
username.send_keys(mail)
password.send_keys(key)
submit = browser.find_element(By.XPATH, value="//button[@type='submit']")
submit.click()
time.sleep(random.randint(1, maxDelay))

for page in range(1, pages_upto):
    searcher_url = f"{url}/search/results/people/?geoUrn=%5B%22103644278%22%2C%22101165590%22%2C%22101174742%22%2C%22103350119%22%2C%22104305776%22%2C%22100456013%22%2C%22101452733%22%2C%22101620260%22%2C%22101728296%22%2C%22102105699%22%2C%22102264497%22%2C%22102890719%22%2C%22103819153%22%2C%22104170880%22%2C%22105072130%22%2C%22105117694%22%2C%22105490917%22%2C%22106670623%22%2C%22106693272%22%5D&keywords={search_param}&network=%5B%22S%22%5D&origin=FACETED_SEARCH&page={page}&serviceCategory=%5B%221275%22%2C%22669%22%2C%2269%22%2C%224044%22%2C%221723%22%2C%222004%22%2C%22482%22%2C%2210048%22%2C%225255%22%2C%221836%22%2C%222174%22%2C%22899%22%2C%2249%22%2C%222269%22%2C%22123%22%2C%22115%22%5D&sid=WRy"

    browser.get(searcher_url)
    time.sleep(random.randint(1, maxDelay))
    buttons = browser.find_elements(By.TAG_NAME, value="button")
    connect_buttons = [btn for btn in buttons if btn.text == "Connect"]
    
    counter = 0
    for btn in connect_buttons:
        browser.execute_script(browser_script, btn)
        time.sleep(random.randint(1, maxDelay))
        ## add note
        addnote = browser.find_element(By.XPATH, value="//button[@aria-label='Add a note']")
        browser.execute_script(browser_script, addnote)
        textArea = browser.find_element_by_id("custom-message")
        textArea.send_keys(message)
        time.sleep(random.randint(1, maxDelay))
        send = browser.find_element(By.XPATH, value="//button[@aria-label='Send now']")
        browser.execute_script(browser_script, send)
        dismiss = browser.find_element(By.XPATH, value="//button[@aria-label='Dismiss']")
        browser.execute_script(browser_script, dismiss)
        time.sleep(random.randint(1, maxDelay))
        counter += 1
        if counter == totalCount:
            print("Messages & invitations sent: " + str(counter))
            browser.quit()
            quit()
        if counter % 3 == 0:
            time.sleep(random.randint(1, maxDelay))