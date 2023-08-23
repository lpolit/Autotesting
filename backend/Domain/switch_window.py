from Domain.step import Step


class SwitchWindow(Step):

    short_name = "switch_window"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.window_name = args["window_name"]
        self._driver = self.get_driver_execution(flow_id)

    def execute(self):
        self._driver.switch_to.window(self.window_name)
        return self.flow_id, None
