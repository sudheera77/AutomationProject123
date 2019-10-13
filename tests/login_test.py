from selenium import webdriver
import pytest
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from utils import utils as utils
import allure
import moment




@pytest.mark.usefixtures("test_setup")
class TestLogin():

    '''
    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver=webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield
        driver.close()
        driver.quit()
        '''


    def test_login(self):#previously we have def test_login(self, test_setup)
        driver=self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()
        '''
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()'''


    def test_logout(self):#prevoiusly  def test_logout(self,test_setup):

        try:
            driver=self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()

            assert self.driver.title =="abc"
            #assert title == "OrangeHRM"
        except AssertionError as error:

            print("assertion error has occured")
            print(error)
            currenttime=moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currenttime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/Sudheera Adusupalli/PycharmProjects/AutomationProject1/screenshots/"+screenshotName+".png")
            raise
        except:
            currenttime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currenttime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(
                "C:/Users/Sudheera Adusupalli/PycharmProjects/AutomationProject1/screenshots/" + screenshotName + ".png")
            print("There was an exception")
            raise
        else:
            print("no exceptions as occured:")
        finally:
            print("i am in finally block:")
        '''
        driver.find_element_by_id("welcome").cpytestlick()
        driver.find_element_by_link_text("Logout").click()
        '''
        #for execution use the below command python -m pytest

    print("Test completed")
    #install package pytest-html
    #for report generation use the belowcommand pytest --html=AutomationProject1/reports/report1.html --self-contained-html
    #for execution use this command pytest --browser firefox
    #for allure reports use the command pytest --alluredir=reports/allure-reports
    #allure serve reports/allure-reports


