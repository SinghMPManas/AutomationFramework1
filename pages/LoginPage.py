class loginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "identifierId"
        self.username_button_xpath = "//span[@class='RveJvd snByac']"
        self.password_textbox_name = "password"
        self.password_button_xpath = "//span[contains(text(),'Next')]"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def click_username_button(self):
        self.driver.find_element_by_xpath(self.username_button_xpath).click()

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_password_button(self):
        self.driver.find_element_by_xpath(self.password_button_xpath).click()