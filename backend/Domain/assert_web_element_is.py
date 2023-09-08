from common.base_waits import BaseWait

from domain.step import Step


class AssertWebElementIs(Step):

    short_name = "assert_web_element_is"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.selector_type = self.get_selector(args["selector_type"])
        self.path_element = args["path_element"]
        self._driver = self.get_driver_execution(flow_id)
        self.base_wait = BaseWait(self._driver)
        self.web_element = self._driver.find_element(self.selector_type, self.path_element)


class AssertIsVisible(AssertWebElementIs):

    short_name = "assert_is_visible"

    def execute(self):
        assert self.web_element.is_displayed()
        return self.flow_id, None


class AssertIsEnabled(AssertWebElementIs):

    short_name = "assert_is_enabled"

    def execute(self):
        assert self.web_element.is_enabled()
        return self.flow_id, None


class AssertIsSelected(AssertWebElementIs):

    short_name = "assert_is_selected"

    def execute(self):
        assert self.web_element.is_selected()
        return self.flow_id, None
