from selenium.webdriver import ActionChains


class BaseStep:

    def __init__(self, driver):
        self.driver = driver

    def change_tab(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def click_element_script(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def close_tab(self):
        self.driver.close()

    def close_and_change_tab(self, index):
        self.close_tab()
        self.change_tab(index)

    def scroll_to_element(self, element, arg):
        self.driver.execute_script(arg, element)

    def get_current_url(self):
        return self.driver.current_url

    def new_tab(self):
        self.driver.switch_to.new_window('tab')

    def new_window(self):
        self.driver.switch_to.new_window('window')

    def set_url(self, url):
        self.driver.get(url)

    def switch_to_frame(self, iframe):
        self.driver.switch_to.frame(iframe)

    def hover_over_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def change_window_by_title(self, title):
        actual_handle = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                return self.driver.switch_to.window(actual_handle)
