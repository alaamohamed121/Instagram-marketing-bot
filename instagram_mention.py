from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# Create an options object to run the browser in headless mode
options = Options()
# options.add_argument("--headless")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)
driver.get(
    "https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm")


def start():
    input("when you are ready press any button:")
    # Find the comment input element
    while True:
        try:
            repy = driver.find_elements(By.XPATH ,"//div[text()='Reply']")
            if repy:
                repy[0].click()
                time.sleep(2)
            comment_bar = driver.find_element(By.CSS_SELECTOR, ".xxxdfa6")
            # Load usernames from file
            
            with open('users.txt', "r") as file:
                data = file.readlines()
            for i in range(2):
                if comment_bar:
                    comment_bar.send_keys("@")
                time.sleep(2)

                time.sleep(2)
                comment_bar = driver.find_element(By.CSS_SELECTOR, ".xwmqs3e")
                if comment_bar:
                    comment_bar.send_keys(data.pop(0).strip())

                with open('users.txt', 'w') as file:
                    # Write the remaining lines back to the file
                    file.writelines(data)

                time.sleep(3)
                comment_bar.send_keys(Keys.ENTER)
                time.sleep(2)
                comment_bar.send_keys(Keys.ENTER)
                time.sleep(2)
                # Add " hi" after the second ENTER
                # comment_bar.send_keys("hi ")
                # time.sleep(2)

            comment_bar.send_keys("hi ")
            time.sleep(40)
            post = driver.find_element(By.CSS_SELECTOR, ".xwhw2v2")
            post.click()
            time.sleep(30)

        except:
            next


start()
