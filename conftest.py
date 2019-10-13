import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Type in browser name eg.chrome OR firefox")

@pytest.fixture(scope="class")
def test_setup(request):
        browser=request.config.getoption("--browser")
        if browser == 'chrome':
            driver=webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        #driver=webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        elif browser == 'firefox':
            driver=webdriver.Firefox(executable_path="../drivers/geckodriver.exe")

        driver.maximize_window()
        request.cls.driver=driver
        driver.implicitly_wait(5)
        yield
        driver.close()
        driver.quit()
