import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from selenium.webdriver.support.wait import WebDriverWait
from pyjavaproperties import Properties
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
class Base_SetUp:


    @pytest.fixture(autouse=True)
    def preconditions(self):
        ppt_obj=Properties()
        ppt_obj.load(open("../config.properties"))
        grid=ppt_obj["GRID"]
        grid_url=ppt_obj["GRID_URL"]
        browser=ppt_obj["BROWSER"]
        ito=ppt_obj["ITO"]
        eto=ppt_obj["ETO"]
        app_url=ppt_obj["APP_URL"]

        if grid.lower()=="yes":
            if browser.lower()=="chrome":
                options=ChromeOptions()
            elif browser.lower()=="firefox":
                options=FirefoxOptions()
            else:
                options=EdgeOptions()

            options=ChromeOptions()
            self.driver=Remote(command_executor=grid_url,  options=options)

        else:
            print("open the browser")
            if browser.lower()=="chrome":
                self.driver=Chrome()
            elif browser.lower()=="firefox":
                self.driver=Firefox()
            else:
                self.driver=Edge()

        print("set implicit timeout",ito,"seconds")
        self.driver.implicitly_wait(ito)
        print("set eto",eto)
        self.wait=WebDriverWait(self.driver,eto,"seconds")
        print("maximize the window")
        self.driver.maximize_window()
        print("enter the url",app_url)
        self.driver.get(app_url)


    @pytest.fixture(autouse=True)
    def postcondition(self):
        yield
        print("close the browser")
        self.driver.close()

