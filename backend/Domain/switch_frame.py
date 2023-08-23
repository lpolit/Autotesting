from common_ui.base_waits import BaseWait

from Domain.step import Step


class SwitchFrame(Step):

    short_name = "switch_frame"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.wait_timeout = args["wait_timeout"]
        self._driver = self.get_driver_execution(flow_id)


class SwitchFrameName(SwitchFrame):

    short_name = "frame_name"

    def __init__(self, flow_id, args):
        super().__init__(flow_id, args)
        self.frame_name = args["frame_name"]

    def execute(self):
        self._driver.switch_to.frame(self.frame_name)
        return self.flow_id, None


class SwitchFrameIndex(SwitchFrame):

    short_name = "frame_index"

    def __init__(self, flow_id, args):
        super().__init__(flow_id, args)
        self.frame_index = args["frame_index"]

    def execute(self):
        self._driver.switch_to.frame(self.frame_index)
        return self.flow_id, None


class SwitchFrameWebElement(SwitchFrame):

    short_name = "frame_web_element"

    def __init__(self, flow_id, args):
        super().__init__(flow_id, args)
        self.selector_type = args["selector_type"]
        self.path_element = args["path_element"]
        self.base_wait = BaseWait(self._driver)

    def execute(self):
        web_element = self._driver.find_element(self.selector_type, self.path_element)
        self.base_wait.wait_for_frame_to_be_available_and_switch_to_it(web_element, self.wait_timeout)
        return self.flow_id, None
