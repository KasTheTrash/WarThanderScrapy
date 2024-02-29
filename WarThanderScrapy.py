from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pyperclip

chrome_options = Options()
chrome_options.add_argument('--headless')  # Ενεργοποίηση του headless mode

driver = webdriver.Chrome(options=chrome_options)

url = 'http://127.0.0.1:8111/'
driver.get(url)

time.sleep(1)

html_content = driver.page_source

driver.quit()

# create a new file(txt) with all the html content of the site 

#with open('page_content.html', 'w', encoding='utf-8') as file:
    #file.write(html_content)

#print("HTML περιεχόμενο εξαγάγθηκε στο αρχείο 'page_content.html'")

soup = BeautifulSoup(html_content, 'html.parser')

# Βρίσκουμε την παραμετρο με id "ind-compass" και παίρνουμε το κείμενό του
compass_element = soup.find(id='ind-compass').text

# περνουμε μόνο την τιμή
compass_value = compass_element.split('=')[-1]

print(compass_value)
# Αντιγράφει την τιμή στο πρόχειρο
pyperclip.copy(compass_value)

copied_value = pyperclip.paste()
print("Το compass εχει αντιγραφη :", copied_value)