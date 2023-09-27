from Domain.step import Step
from main import plani


class CloseBrowser(Step):
    short_name = "close_browser"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self._driver = self.get_driver_execution(flow_id)

    def execute(self):
        #self._driver.close()
        self._driver.quit()
        plani.pop(self.flow_id)
        return 0, None
