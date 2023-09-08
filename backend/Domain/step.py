from common.base_step import BaseStep
from common.base_waits import BaseWait
from selenium.webdriver.common.by import By

from main import plani


class Step():

    def __init__(self, flow_id):
        self.flow_id = self.set_new_flow(flow_id)

    def execute(self):
        pass

    def get_selector(self, selector):
        return {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH
        }[selector]

    def set_new_flow(self, flow_id):
        if flow_id == 0:
            id = len(plani.keys()) + 1
            plani[id] = None
            return id
        else:
            return flow_id

    def get_driver_execution(self, flow_id):
        if flow_id == 0:
            raise Exception("No puedo correr sin contexto")
        return plani[flow_id]
