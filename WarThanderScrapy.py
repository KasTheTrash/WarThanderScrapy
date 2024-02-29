from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pyperclip

chrome_options = Options()
chrome_options.add_argument('--headless')  # Enables headless mode

driver = webdriver.Chrome(options=chrome_options)

url = 'http://127.0.0.1:8111/'
driver.get(url)

time.sleep(1)

html_content = driver.page_source

driver.quit()

# create a new file(txt) with all the html content of the site 

#with open('page_content.html', 'w', encoding='utf-8') as file:
    #file.write(html_content)

#print("HTML file 'page_content.html'")

soup = BeautifulSoup(html_content, 'html.parser')

# We find the parameter with id "ind-compass" and get its text
compass_element = soup.find(id='ind-compass').text

# we only pass the price
compass_value = compass_element.split('=')[-1]

print(compass_value)
# Copies the value to the clipboard
pyperclip.copy(compass_value)

copied_value = pyperclip.paste()
print("The compass has a copy :", copied_value)
