import time
import pytest
import allure
import moment
from pages.HomePage import HomePage
from pages.LoginPage import loginPage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestGmail_login():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = loginPage(driver)
        login.enter_username(utils.USERNAME)
        login.click_username_button()
        time.sleep(2)
        login.enter_password(utils.PASSWORD)
        login.click_password_button()
        time.sleep(4)
        home = HomePage(driver)
        home.click_menu_icon()
        home.click_Gmail_icon()
        time.sleep(2)
        try:
            titlePage = driver.title
            assert titlePage == "Googl Account"
            print("User logged into", titlePage, "Successfully!")
            time.sleep(2)

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currtime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testname = utils.whoami()
            screenshotname = testname+"_"+currtime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotname, attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/Sadhana/PycharmProjects/AutomationFramework1/screenshots/"+ screenshotname + ".png")
            raise

        else:
            print("No exceptions occurred")

        finally:
            print("We are inside finally block")

    def test_logout(self):
        driver = self.driver
        home = HomePage(driver)
        home.click_username_icon()
        home.click_signout_button()






