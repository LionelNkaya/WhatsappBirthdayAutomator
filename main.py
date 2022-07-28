'''
This programs uses Selenium Web Driver to automate Google Chrome.
The programs opens Chrome goes on Whatsapp and send messages.

Credit:
How to use Selenium browser to automate Whatsapp: https://www.youtube.com/watch?v=eela1UYObWE
'''

from birthday_checker import  birthday_checker
import sys, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# Setting up webdriver for Crhome and adding cache information as argument for Whatsapp to remember the user
options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:/Users/lnkaya/AppData/Local/Google/Chrome/User Data/lnkaya')
options.add_argument('--profile-directory=lnkaya')

chrome_browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= options)
chrome_browser.get('https://web.whatsapp.com/')
time.sleep(100) # Pausing 20 seconds to scan Whatsapp QR code or to wait for Whatsapp to load

msg = 'Happy birthday my dear friend. Tons of love from your bro Lionel'

def opening_new_chat(user_name):
    new_chat = chrome_browser.find_element(By.CLASS_NAME, '_3Qnsr')
    new_chat.send_keys(user_name)
    time.sleep(2)
    
    try:
        user = chrome_browser.find_element(By.XPATH, '//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException as se:
        print('Username not in contact list')
    except Exception as e:
        chrome_browser.close()
        print(e)
        sys.exit()



list_of_friend_with_birthday_today = birthday_checker()

for friend in list_of_friend_with_birthday_today:
    #Looking for the friend in the main Whatsapp left panel
    try: 
        user = chrome_browser.find_element(By.XPATH, '//span[@title="{}"]'.format(friend))
        user.click()
    # If friend not already in main window open a new chat
    except NoSuchElementException as se:
        opening_new_chat(friend)
        time.sleep(1)

    # Finding the box to write the message
    time.sleep(3)
    message_box = chrome_browser.find_element(By.CLASS_NAME, 'p3_M1')
    message_box.click()
    time.sleep(3)
    # Inputting message
    message_box.send_keys(msg)
    time.sleep(3)
    # Clicking on the button to send the message
    message_box = chrome_browser.find_element(By.CLASS_NAME, '_1Ae7k')
    message_box.click()
    time.sleep(3)

chrome_browser.close()
chrome_browser.quit()
sys.exit()


'''
Review: 
- Write a script that adds users to DB - Done in data.py
- Write a script that checks everyday if someone has a birthday - Done in birthday_checker.py
- Write that sends a message using a name as argument - Done in main.py
- To get this script to run everyday using Windows Task Scheduler instructions are avaialbe here - https://www.geeksforgeeks.org/schedule-a-python-script-to-run-daily
'''