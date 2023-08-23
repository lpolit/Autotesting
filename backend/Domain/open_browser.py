from Domain.step import Step
from common_ui.driver import Driver
from main import plani


class OpenBrowser(Step):
    short_name = "open_browser"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.browser = args["browser"]
        self.url = args["url"]
        self.window_state = args["window_state"]
        self.wait_timeout = args["wait_timeout"]
        self.headless = args["headless"]

    def execute(self):
        if plani[self.flow_id] is None:
            _driver = Driver().get_driver(self.browser, self.headless)
            self.set_driver_execution(_driver)
        _driver.implicitly_wait(self.wait_timeout)
        _driver.get(self.url)
        if self.window_state.lower() == "maximizado":
            _driver.maximize_window()
        elif self.window_state.upper() == "minimizado":
            _driver.minimize_window()
        return self.flow_id, None

    def set_driver_execution(self, driver):
        plani[self.flow_id] = driver

