



class Test_DemoClass:
    #prefix => test_

    def setup_method(self): #her test başlangıcında çalışır
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()

    def teardown_methos(self): #her testinin bitiminde çalışıcak fonk
        self.driver.quit()


    def test_demo(self):
        text = "x"
        assert text == "x"
    def test_deneme(self):
        text = "x"
        assert text == "x"




        