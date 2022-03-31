import sys, time
import ast
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Reading input file: 
with open('input.txt') as f:
     data = f.read()

# Building the Python Dictionary using the ast.literal_eval() function and my data variable as argument
user_dict = ast.literal_eval(data)

today = date.today().strftime('%m/%d/%Y')
current_time = datetime.now().strftime("%H:%M:%S")

msgTime = '1:00:00'
msg = 'Happy birthday my dear friend. From your bro Lionel'

def new_chat(user_name):
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

# Setting up webdriver for Crhome and adding cache information as argument for Whatsapp to remember the users
options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:/Users/Lionel.Nkaya/AppData/Local/Google/Chrome/User Data/Default')
options.add_argument('--profile-directory=Default')

#chrome_browser = webdriver.Chrome(executable_path=r'C:/Users/Lionel.Nkaya/Downloads/chromedriver.exe', options= options)
chrome_browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= options)
chrome_browser.get('https://web.whatsapp.com/')
time.sleep(7) # Pausing to scan Whatsapp QR code


if __name__ == '__main__':
    while True:
        user_DOB_list = list(user_dict.values()) 
        for user_DOB in user_DOB_list:
            if user_DOB == today:
                user_name_list = list(user_dict.keys())
                for user_name in user_name_list: 
                    try:
                        user = chrome_browser.find_element(By.XPATH, '//span[@title="{}"]'.format(user_name))
                        user.click()
                    except NoSuchElementException as se:
                        new_chat(user_name)
                        time.sleep(1)

                    # Finding the box to write the message
                    time.sleep(3)
                    message_box = chrome_browser.find_element(By.CLASS_NAME, 'p3_M1')
                    message_box.click()
                    time.sleep(3)
                    # Inputting message
                    message_box.send_keys(msg)
                    time.sleep(3)
                    # Clicking on the button to close
                    message_box = chrome_browser.find_element(By.CLASS_NAME, '_4sWnG')
                    message_box.click()
                    time.sleep(2)
                    #chrome_browser.close()
                    #Ssys.exit()
                    
                #The program reruns every 12 hours ( 12 h = 43200 seconds)
                #today = date.today().strftime('%m/%d/%Y')
                #time.sleep(5)          

'''
Review 03/30/22: 
- Write a script that adds users to DB 
- Write a script that checks everyday if someone has a birthday
- If yes it runs this main script with argument username
'''