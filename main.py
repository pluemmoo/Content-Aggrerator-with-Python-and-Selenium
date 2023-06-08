from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import json

# Set the path to your Firefox driver executable
driver_path = '/home/jasonblue/Firefoxdriver/geckodriver'

# Create a Firefox driver instance
options = FirefoxOptions()
driver = webdriver.Firefox(options=options)

# Open the desired webpage
driver.get('https://liquipedia.net/')

# Use Selenium to interact with the webpage
elements = driver.find_elements(By.CLASS_NAME, 'card')

titles = []
descriptions = []
# Extract the desired information from the elements
for element in elements:
    title = element.find_element(By.CLASS_NAME, 'card__title-link').text
    titles.append(title)
    description = element.find_element(By.CLASS_NAME, 'card__list').text
    descriptions.append(description)
    # print(f'Title: {titles}')
    # print(f'Description: {descriptions}')

data = {}
for i in range(len(titles)):
    key = f'Title: {titles[i]}'
    value = f'Competitions: \n{descriptions[i]}'
    data[key] = value


with open('card_data.json', 'w') as file:
    json.dump(data, file, indent=4)
# Close the web driver to release system resources
driver.quit()