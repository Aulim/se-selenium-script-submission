from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

def manipulation1():
    # Untuk Mengubah Text Input Field dengan id "myTextInput" menjadi "Andrean Gusman Djabbar"
    driver.find_element(by="id", value="myTextInput").send_keys("Andrean Gusman Djabbar")

def manipulation2():
    # Untuk Mengubah Text Area Field dengan id "myTextarea" menjadi "Computer Science"
    driver.find_element(by="id", value="myTextarea").send_keys("Computer Science")

def manipulation3():
    # Untuk Mengklik Button dengan id "myButton"
    driver.find_element(by="id", value="myButton").click()

def manipulation4():
    # Untuk Mengubah Dropdown dengan id "mySelect" menjadi "100%"
    dropdown = driver.find_element(by="id", value="mySelect")
    select = Select(dropdown)
    select.select_by_value("100%")

def manipulation5():
    # Untuk Mengubah Slider dengan id "mySlider" menjadi 100
    slider = driver.find_element(by="id", value="mySlider")
    driver.execute_script("arguments[0].value = arguments[1];", slider, 100)
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", slider)

manipulation1()
manipulation2()
manipulation3()
manipulation4()
manipulation5()

os.system("cls")
input("Press Enter to Exit...")
driver.quit()
