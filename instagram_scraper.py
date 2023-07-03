from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Create an options object to run the browser in headless mode
options = Options()
# options.add_argument("--headless")


# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)
driver.get("https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm")
option = input("scrape followers(1) , scrape likes(2):")
time.sleep(3)
def followers():
    usernamee =input("username:")
    driver.get("https://www.instagram.com/"+usernamee+"/followers/")
    input("when you are ready press any button:")

    while True:
        choice = input("Enter 1 to extract users, or any other key to exit: ")
        if choice == "1":
            # Find all the a tags
            links = driver.find_elements(By.CLASS_NAME, "_ab8y")
            # Create a file to write the links
            with open("users.txt", "a") as file:
                # Iterate over the list of links
                for link in links:
                    link = link.text
                    
                    file.write("@" +link + "\n")

            # Close the web driver
            # Remove duplicates from the file
            file_path = "users.txt"
            remove_duplicates_from_file(file_path)
        else:
            break
            driver.quit()



def likes():

    while True:
        choice = input("Enter 1 to extract users, or any other key to exit: ")
        
        if choice == "1":
            # Find all the a tags
            links = driver.find_elements(By.XPATH, "//div[@class='x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1']")

            # Create a file to write the links
            with open("users.txt", "a") as file:
                # Iterate over the list of links
                for link in links:
                    link = link.text
                    file.write("@" +link + "\n")

            # Remove duplicates from the file
            file_path = "users.txt"
            remove_duplicates_from_file(file_path)

        else:
            driver.quit()
            break

def remove_duplicates_from_file(file_path):
    # Create an empty set to store unique elements
    unique_lines = set()
    # Open the file for reading
    with open(file_path, "r") as file:
        # Read each line of the file
        lines = file.readlines()
        # Iterate over the lines
        for line in lines:
            # Remove the newline character from the end of the line
            line = line.strip()
            # If the line is not in the set, add it
            if line not in unique_lines:
                unique_lines.add(line)
    # Write the unique lines back to the file
    with open(file_path, "w") as file:
        for line in unique_lines:
            file.write(line + "\n")






if option == "1":
    followers()
elif option == "2":
    likes()
