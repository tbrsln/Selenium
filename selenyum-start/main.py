#otomasyon testinden önce manuel test gereklidir

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()   #ekranı büyütür
sleep(5) #ekranda 5 sn gözükmesni sağlıyor

input = driver.find_element(By.NAME,"q")
input.send_keys("kodlamaio")
sleep(2)

searchButton = driver.find_element(By.NAME,"btnK")
searchButton.click()
sleep(2)

firstResult = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
firstResult.click()
sleep(5)

listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
testResult = len(listOfCourses) == 6 # == diyerek kontrol sağlıyorum
print(f"Test Sonucu: {testResult}") #False sonucunu döndürdü çünkü 7 tane var 

