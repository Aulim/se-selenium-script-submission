from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os

# Inisialisasi driver untuk Chrome
driver = webdriver.Chrome()

# Buka halaman demo dari SeleniumBase
driver.get("https://seleniumbase.io/demo_page")

def manipulation1():
    # Mengubah teks pada input field dengan id "myTextInput" menjadi "Ananda Madani"
    driver.find_element(by="id", value="myTextInput").send_keys("Ananda Madani")

def manipulation2():
    # Mengubah teks pada area teks dengan id "myTextarea" menjadi "Computer Science"
    driver.find_element(by="id", value="myTextarea").send_keys("Computer Science")

def manipulation3():
    # Mengklik tombol dengan id "myButton"
    driver.find_element(by="id", value="myButton").click()

def manipulation4():
    # Mengubah pilihan dropdown dengan id "mySelect" menjadi "100%"
    dropdown = driver.find_element(by="id", value="mySelect")
    select = Select(dropdown)
    select.select_by_value("100%")

def manipulation5():
    # Menggeser slider dengan id "mySlider" ke nilai 100
    slider = driver.find_element(by="id", value="mySlider")
    driver.execute_script("arguments[0].value = arguments[1];", slider, 100)
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", slider)

# Menjalankan fungsi-fungsi manipulasi
manipulation1()
manipulation2()
manipulation3()
manipulation4()
manipulation5()

# Membersihkan layar dan menunggu input sebelum keluar
os.system("cls")
input("Press Enter to Exit...")
driver.quit()
