from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Test_SauceDemoWork:
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.get("http://www.saucedemo.com")
        driver.maximize_window()  
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID,"password")


        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(5)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu: {testResult}")
        sleep(3)

    def test_blank_fields(self):
        driver = webdriver . Chrome ()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        sleep(3)
        print(f"Test Sonucuu : {testResult}")
        sleep(3)

    def test_blank_password(self):
        driver = webdriver.Chrome()
        driver.get("http://saucedemo.com/")
        driver.maximize_window()

        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        sleep(3)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text =="Epic sadface: Password is required"
        sleep(3)
        print(f"Test Sonucu: {testResult}")
        sleep(3)

    def test_successfully_login(self):
        driver = webdriver.Chrome()
        driver.get("http://saucedemo.com/")
        driver.maximize_window()

        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(3)
        current_url = driver.current_url
        if current_url == "https://www.saucedemo.com/inventory.html":
            print("Başarıyla yönlendirildi.")
        else:
            print("Yönlendirme başarısız oldu.")

        sleep(3)
        listOfProduct = driver.find_elements(By.CLASS_NAME, "inventory_item_label")
        testResult = len(listOfProduct) == 6
        print(f"Test Sonucu : {testResult}")


testClass = Test_SauceDemoWork()
testClass.test_invalid_login()
testClass.test_blank_fields()
testClass.test_blank_password()
testClass.test_successfully_login()
