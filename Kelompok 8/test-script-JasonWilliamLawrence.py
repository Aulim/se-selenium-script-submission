from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your ChromeDriver executable 
webdriver_service = Service(r'C:\Users\ASUS\Desktop\se-selenium-script-submission\Kel_8\chromedriver.exe') 

options = Options()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(service=webdriver_service, options=options) 

driver.get('https://demoqa.com/text-box')

# input email
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'userEmail'))
)
email_input.send_keys('jason.lawrence@binus.ac.id')

# input nama
nama_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'userName'))
)
nama_input.send_keys('Jason W')

# input password
alamat_textarea = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'txt_pwd'))
)
alamat_textarea.send_keys('asdasdasd')

# click submit
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'submit'))
)
submit_button.click()


# cek apakah data ada di element
# email
output_email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'email'))
)
assert 'jason.lawrence@binus.ac.id' in output_email.text

# nama
output_nama = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'name'))
)
assert 'Jason W' in output_nama.text

driver.quit()
