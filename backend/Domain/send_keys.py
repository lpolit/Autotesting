from selenium.webdriver import Keys

from common.base_waits import BaseWait

from domain.step import Step


class SendKeys(Step):

    short_name = "send_keys"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.selector_type = self.get_selector(args["selector_type"])
        self.path_element = args["path_element"]
        self.text_to_send = args["text_to_send"]
        self.wait_timeout = args["wait_timeout"]
        self.enter_key = args["enter_key"]
        self._driver = self.get_driver_execution(flow_id)
        self.base_wait = BaseWait(self._driver)
        self.web_element = self._driver.find_element(self.selector_type, self.path_element)

    def execute(self):
        self.base_wait.wait_for_element_to_be_clickable(self.web_element, self.wait_timeout)
        self.web_element.send_keys(self.text_to_send)
        self.web_element.send_keys(Keys.ENTER) if self.enter_key else None
        return self.flow_id, None
