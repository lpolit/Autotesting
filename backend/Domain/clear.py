from common_ui.base_waits import BaseWait

from Domain.step import Step


class Clear(Step):
    short_name= "clear"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.selector_type = self.get_selector(args["selector_type"])
        self.path_element = args["path_element"]
        self.wait_timeout = args["wait_timeout"]
        self._driver = self.get_driver_execution(flow_id)
        self.base_wait = BaseWait(self._driver)
        self.web_element = self._driver.find_element(self.selector_type, self.path_element)

    def execute(self):
        self.base_wait.wait_for_element_to_be_clickable(self.web_element, self.wait_timeout)
        self.web_element.clear()
