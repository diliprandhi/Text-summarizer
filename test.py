from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace with the path to your chromedriver executable
driver = webdriver.Chrome('path/to/chromedriver')

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for user to scan the QR code
input('Press Enter after scanning QR code...')

# Find the chat or group you want to send messages to
chat_name = 'Chat or Group Name'
search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
search_box.send_keys(chat_name)
search_box.send_keys(Keys.ENTER)

# Wait for the chat to load
time.sleep(2)

# Send continuous messages
message = 'Hello, World!'
while True:
    message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    time.sleep(1)

# Close the browser
driver.quit()