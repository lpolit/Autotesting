import base64

from common.base_waits import BaseWait

from Domain.step import Step
from common.screenshot import Screenshot as Screen


class Screenshot(Step):

    short_name = "screenshot"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.selector_type = self.get_selector(args["selector_type"])
        self.path_element = args["path_element"]
        self.wait_timeout = args["wait_timeout"]
        self._driver = self.get_driver_execution(flow_id)
        self.base_wait = BaseWait(self._driver)


class ScreenshotPage(Screenshot):

    short_name = "screenshot_page"

    def execute(self):
        img = Screen.take_screenshot(self._driver, self.short_name + FileUtils.get_actual_date_time('%H:%M:%S')).image
        return self.flow_id, base64.encodebytes(img)


class ScreenshotFullPage(Screenshot):

    short_name = "screenshot_full_page"

    def execute(self):
        img = Screen.take_fullpage_screenshot(self._driver, self.short_name+FileUtils.get_actual_date_time('%H:%M:%S')).image
        return self.flow_id, base64.encodebytes(img)


class ScreenshotWebElement(Screenshot):

    short_name = "screenshot_web_element"

    def execute(self):
        web_element = self._driver.find_element(self.selector_type, self.path_element)
        img =  Screen.take_web_element_screenshot(web_element, self.short_name+FileUtils.get_actual_date_time('%H:%M:%S')).image
        return self.flow_id, base64.encodebytes(img)
