from common.base_waits import BaseWait

from Domain.step import Step


class SwitchAlert(Step):

    short_name= "switch_alert"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.button_type = args["button_type"]
        self._driver = self.get_driver_execution(flow_id)


class SwitchAlertAccept(SwitchAlert):

    short_name = "alert_accept"

    def execute(self):
        self._driver.switch_to.alert().accept()
        return self.flow_id, None


class SwitchAlertDismiss(SwitchAlert):

    short_name = "alert_dismiss"

    def execute(self):
        self._driver.switch_to.alert().dismiss()
        return self.flow_id, None
