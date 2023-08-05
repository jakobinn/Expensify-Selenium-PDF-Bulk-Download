#https://googlechromelabs.github.io/chrome-for-testing/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import opencsv
import prog_settings
import os
import urllib.request

### INITIALIZATION ###

# Path to chromedriver executable (adjust as needed)
driver_path = './chromedriver'

chrome_options = Options()

# set download directory
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": prog_settings.PROGRAM_DIR,
    "download.prompt_for_download": False, # to disable download prompt
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": False  # to automatically open downloaded files
})

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.expensify.com/expenses")

### LOGIN ###

loginTypeButton = driver.find_element(By.ID, "js_click_showEmailForm")
loginTypeButton.click()

time.sleep(0.2)

loginInput = driver.find_element(By.ID, "login")
loginInput.send_keys(prog_settings.USERNAME)

time.sleep(0.2)

nextButton = driver.find_element(By.ID, "js_click_submitLogin")
nextButton.click()

time.sleep(20)

### GETTING THE DEFAULT CSV FILE ###

startDate = driver.find_element(By.ID, "startDate")
startDate.send_keys("2023-07-25")

endDate = driver.find_element(By.ID, "endDate")
endDate.send_keys("2023-07-31")

selectAllCheckbox = driver.find_element(By.ID, "selectAllExpenses")
selectAllCheckbox.click()

csvFile = driver.find_element_by_xpath('//a[@role="button" and @tabindex="-1" and @data-toggle="tooltip"]')
csvFile.click()

receipts = opencsv.getReceiptData("Bulk_Expense_Export.csv")
print(receipts)

### DOWNLOADING THE PDF FILES INTO A FOLDER OF YOUR CHOICE ###

for line in receipts:
    link = opencsv.getLink(line)
    driver.get(link)
    time.sleep(1)
    submitButton = driver.find_element(By.XPATH, "//*[text()='Download a Copy']")
    submitButton.click()
    time.sleep(2)
    current_url = driver.current_url
    print(current_url)
    filename = opencsv.getPDFFileName(line)
    filepath = prog_settings.PATH_URL + filename + opencsv.getFileType(current_url)

    print(filepath)

    if os.path.isfile(filepath):
        print("File already exists")
        continue
    
    time.sleep(1)

    urllib.request.urlretrieve(current_url, filepath)


driver.quit()

