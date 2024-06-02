from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

# mengganti myTextInput menjadi "Dunia itu World"
driver.find_element(by="id", value="myTextInput").send_keys("Dunia itu World")

# mengganti placeholderText menjadi "Anda Siapa?"
driver.find_element(by="id", value="placeholderText").send_keys("Anda Siapa?")

# mengganti myTextarea menjadi "Bukan warna Biru?"
driver.find_element(by="id", value="myTextarea").send_keys("Bukan warna Biru")

# mengganti myButton menjadi clicked dr not clicked
driver.find_element(by="id", value="myButton").click()

# mengganti chcekBox1 menjadi clicked dr not clicked
driver.find_element(by="id", value="checkBox1").click()

#mengganti value dari slider dr 25% ke 75%
def dropdown():
    dropdown = driver.find_element(by="id", value="mySelect")
    select = Select(dropdown)
    select.select_by_value("75%")

dropdown()

input("")
driver.quit()