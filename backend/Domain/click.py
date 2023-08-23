from common_ui.base_waits import BaseWait
from selenium.webdriver import ActionChains

from Domain.step import Step


class Click(Step):

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.selector_type = self.get_selector(args["selector_type"])
        self.path_element = args["path_element"]
        self.wait_timeout = args["wait_timeout"]
        self._driver = self.get_driver_execution(flow_id)
        self.base_wait = BaseWait(self._driver)
        self.web_element = self._driver.find_element(self.selector_type, self.path_element)

    def wait(self):
        self.base_wait.wait_for_element_to_be_clickable(self.web_element, self.wait_timeout)


class ClickLeft(Click):

    short_name = "click_left"

    def execute(self):
        self.wait()
        self.web_element.click()
        return self.flow_id, None


class ClickRight(Click):

    short_name = "click_right"

    def execute(self):
        self.wait()
        action_chains = ActionChains(self._driver)
        action_chains.context_click(self.web_element).perform()


class ClickMiddle(Click):

    short_name = "click_middle"

    def execute(self):
        self.wait()
        self.web_element.click()


class ClickDouble(Click):

    short_name = "click_double"

    def execute(self):
        self.wait()
        self.web_element.click()
