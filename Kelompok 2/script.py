from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Inisialisasi driver (Pastikan Anda telah menginstal WebDriver untuk browser yang Anda gunakan)
driver = webdriver.Chrome()

# Ganti dengan URL halaman web yang ingin Anda uji
driver.get("https://seleniumbase.io/demo_page")

def select_function1():
    # Pilih elemen dropdown dengan id 'mySelect'
    select = Select(driver.find_element_by_id('mySelect'))
    
    # Mendapatkan nilai yang dipilih dari dropdown
    selected_option = select.first_selected_option.text
    
    # Pilih elemen meter dan label dengan id masing-masing
    meter = driver.find_element_by_id('meterBar')
    meter_label = driver.find_element_by_id('meterLabel')
    
    # Mengotomasi perubahan nilai meter dan label berdasarkan pilihan dropdown
    if selected_option == "25%":
        meter.set_attribute('value', '0.25')
        meter_label.text = "HTML Meter: (25%)"
    elif selected_option == "50%":
        meter.set_attribute('value', '0.5')
        meter_label.text = "HTML Meter: (50%)"
    elif selected_option == "75%":
        meter.set_attribute('value', '0.75')
        meter_label.text = "HTML Meter: (75%)"
    elif selected_option == "100%":
        meter.set_attribute('value', '1.0')
        meter_label.text = "HTML Meter: (100%)"

def click_link1():
    # Temukan elemen h3 dan ubah teks kontennya
    the_h3 = driver.find_element_by_tag_name('h3')
    the_h3.text = "Link One Selected"
    
    # Temukan elemen dengan class 'dropdown-content' dan ubah style pointerEvents menjadi 'none'
    overlay = driver.find_element_by_class_name('dropdown-content')
    driver.execute_script("arguments[0].style.pointerEvents='none';", overlay)

def reveal_row(checkbox_element):
    # Temukan elemen baris yang tersembunyi
    hidden_row = driver.find_element(By.CSS_SELECTOR, 'tr.hidden_row')
    
    # Periksa status checkbox dan tampilkan atau sembunyikan baris sesuai
    if checkbox_element.is_selected():
        # Jika checkbox dicentang, tampilkan baris
        driver.execute_script("arguments[0].style.display='';", hidden_row)
    else:
        # Jika checkbox tidak dicentang, sembunyikan baris
        driver.execute_script("arguments[0].style.display='none';", hidden_row)

# Temukan elemen checkbox pertama dan tambahkan event listener untuk click
first_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]:first-child')
ActionChains(driver).click(first_checkbox).perform()

# Panggil fungsi dengan elemen checkbox sebagai argumen untuk menjalankan otomasi
reveal_row(first_checkbox)
click_link1()
select_function1()
