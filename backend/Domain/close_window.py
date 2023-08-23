from Domain.step import Step


class CloseWindow(Step):
    short_name = "close_window"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)

    def execute(self):
        self.close_tab()
        return self.flow_id, None
