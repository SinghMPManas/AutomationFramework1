class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.menu_icon_classname = "gb_D"
        self.gmail_icon_xpath = "//a[@id='gb23']//span[@class='gb_r']"
        self.Username_icon_xpath = "//span[@class='gb_Ia gbii']"
        self.signout_button_id = "gb_71"

    def click_menu_icon(self):
        self.driver.find_element_by_class_name(self.menu_icon_classname).click()

    def click_Gmail_icon(self):
        self.driver.find_element_by_xpath(self.gmail_icon_xpath).click()

    def click_username_icon(self):
        self.driver.find_element_by_xpath(self.Username_icon_xpath).click()

    def click_signout_button(self):
        self.driver.find_element_by_id(self.signout_button_id).click()

