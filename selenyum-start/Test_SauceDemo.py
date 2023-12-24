from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı yanıt alana kadar bekletiyor
from selenium.webdriver.support import expected_conditions  as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains

class Test_SauceDemo:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.saucedemo.com")
        self.driver.maximize_window()  
        
        
    def test_invalid_login(self):
        self.driver.get("http://www.saucedemo.com")
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput.send_keys("locked_out_user")
        
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        passwordInput.send_keys("secret_sauce")
       
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")

    def valid_login(self):
        self.driver.get("http://www.saucedemo.com")

        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput.send_keys("standart_user")
        
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        passwordInput.send_keys("secret_sauce")
       
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        headerLogo = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")))
        testResult = header.Logo.text == "Swag Labs"
        print(f"TEST SONUCU: {testResult}")


testClass = Test_SauceDemo()
testClass.test_invalid_login()
testClass.valid_login()