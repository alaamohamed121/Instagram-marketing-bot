from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


# Create an options object to run the browser in headless mode


path = input("enter file path:")
options = Options()

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)
driver.get("https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm")

def start():
    start = input("start:")
    with open("users.txt", "r") as file:
        lines = file.readlines()
    while lines:
        for i in range(1):
            try:
                driver.get("https://www.instagram.com/direct/new/")
                search = driver.find_element(By.XPATH, "//input[@type='text']")
                search.send_keys(lines[0])
                lines.pop(0)
                time.sleep(5)
                with open("users.txt", "w") as file:
                    file.writelines(lines)
                button = driver.find_elements(By.XPATH, "//button[@class='_abl-']")
                button[0].click()
                time.sleep(3)
                next_button = driver.find_elements(By.XPATH, "//div[text()='Next']")
                next_button[0].click()
                time.sleep(5)
                
                # Locate the photo upload input element
                upload_input = driver.find_element(By.XPATH, "//input[@type='file']")

                # Send the path of the photo file to the upload input element
                # Change the path to the actual path of the photo on your computer
                upload_input.send_keys(path)
                
                # Wait for the upload to complete
                time.sleep(10)
                
                # Enter the message and send it
                message = driver.find_element(By.XPATH, '//textarea[@placeholder="Message..."]')
                message.send_keys(Keys.CONTROL, 'v')
                time.sleep(5)

                message.send_keys(Keys.RETURN)
                time.sleep(30)
            except:
                next

start()
