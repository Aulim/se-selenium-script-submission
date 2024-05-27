from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your ChromeDriver executable 
webdriver_service = Service(r'C:\Users\User\se-selenium-script-submission\Kelompok 8\chromedriver.exe') 

# Create options to ignore certificate errors
options = Options()
options.add_argument('--ignore-certificate-errors')

# Create the Chrome WebDriver instance
driver = webdriver.Chrome(service=webdriver_service, options=options) 

# Buka halaman web testing (ganti URL sesuai halaman yang akan diuji)
driver.get('https://demoqa.com/text-box')

# Temukan elemen input nama dan isi dengan teks
nama_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'userName'))
)
nama_input.send_keys('Calvin Hendra')

# Temukan elemen input email dan isi dengan teks
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'userEmail'))
)
email_input.send_keys('calvin@gmail.com')

# Temukan elemen textarea alamat dan isi dengan teks
alamat_textarea = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'currentAddress'))
)
alamat_textarea.send_keys('Jl. Salam Raya')

# Temukan tombol submit dan klik
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'submit'))
)
submit_button.click()

# Verifikasi bahwa data yang dimasukkan muncul di output
output_nama = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'name'))
)
assert 'Calvin Hendra' in output_nama.text

output_email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'email'))
)
assert 'calvin@gmail.com' in output_email.text

# Tutup browser
driver.quit()
