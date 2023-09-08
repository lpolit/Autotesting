from web_services.ws_core import WsCore

def test_wait_title_is(endpoint_flow, titulo = "Acceso con Clave Fiscal - AFIP"):

    body = {
        "comando": "wait_title_is",
        "argumentos": { "selector_type": "id",
                        "path_element": "",
                        "wait_timeout": "10",
                        "text_value": titulo,
                        "state_type": ""
                       },
        "flow_id": 1
    }
    response = WsCore.execute_request_post(endpoint=endpoint_flow, json=body)
    assert response.status_code == 200

def test_wait_title_contains(endpoint_flow, titulo = "AFIP"):
    body = {
        "comando": "wait_title_contains",
        "argumentos": { "selector_type": "id",
                        "path_element": "",
                        "wait_timeout": "10",
                        "text_value": titulo,
                        "state_type": ""
                       },
        "flow_id": 1
    }
    response = WsCore.execute_request_post(endpoint=endpoint_flow, json=body)
    assert response.status_code == 200

def test_wait_element_is_presence(endpoint_flow, selector="xpath", path="//*[@id='F1:username']"):

    body = {
        "comando": "wait_element_is_presence",
        "argumentos": {"selector_type": selector,
                       "path_element": path,
                       "wait_timeout": "10",
                       "text_value": "",
                       "state_type": ""
                       },
        "flow_id": 1
    }
    response = WsCore.execute_request_post(endpoint=endpoint_flow, json=body)
    assert response.status_code == 200

def test_wait_url_contains(endpoint_flow, url="afip"):
    body = {
        "comando": "wait_url_contains",
        "argumentos": {"selector_type": "id",
                       "path_element": "",
                       "wait_timeout": "10",
                       "text_value": url,
                       "state_type": ""
                       },
        "flow_id": 1
    }
    response = WsCore.execute_request_post(endpoint=endpoint_flow, json=body)
    assert response.status_code == 200



##################################################################################################


"""
 class WaitUrlMatches(Wait):
    short_name="wait_url_matches"

    def execute(self):
        self.base_wait.wait_for_url_matches(self.text_value, self.wait_timeout)

class WaitUrlChanges(Wait):
    short_name="wait_url_changes"

    def execute(self):
        self.base_wait.wait_for_url_changes(self.text_value, self.wait_timeout)

class WaitUrlToBe(Wait):
    short_name="wait_url_to_be"

    def execute(self):
        self.base_wait.wait_for_url_to_be(self.text_value, self.wait_timeout)

class WaitElementToBeVisible(Wait):
    short_name="wait_element_to_be_visible"

    def execute(self):
        self.base_wait.wait_for_element_to_be_visible_locator(*self.get_locator(), self.wait_timeout)

class WaitAllElementsIsPresence(Wait):
    short_name="wait_all_elements_is_presence"

    def execute(self):
        self.base_wait.wait_for_all_elements_is_presence(*self.get_locator(), self.wait_timeout)


class WaitAnyElementToBeVisible(Wait):
    short_name="wait_any_element_to_be_visible"

    def execute(self):
        self.base_wait.wait_for_any_element_to_be_visible_locator(*self.get_locator(), self.wait_timeout)


class WaitAllElementsToBeVisible(Wait):
    short_name="wait_all_elements_to_be_visible"

    def execute(self):
        self.base_wait.wait_for_all_elements_to_be_visible_locator(*self.get_locator(), self.wait_timeout)


class WaitElementToBeTextIsPresent(Wait):
    short_name="wait_element_to_be_text_is_present"

    def execute(self):
        self.base_wait.wait_for_element_to_be_text_is_present(*self.get_locator(), self.wait_timeout)


class WaitElementTextValueIsPresent(Wait):
    short_name="wait_element_text_value_is_present"

    def execute(self):
        self.base_wait.wait_for_element_text_value_is_present(*self.get_locator(), self.wait_timeout)


class WaitFrameToBeAvailableAndSwitchToIt(Wait):
    short_name="wait_frame_to_be_available_and_switch_to_it"

    def execute(self):
        self.base_wait.wait_for_frame_to_be_available_and_switch_to_it(*self.get_locator(), self.wait_timeout)


class WaitElementToBeInvisible(Wait):
    short_name="wait_element_to_be_invisible"

    def execute(self):
        self.base_wait.wait_for_element_to_be_invisibe_locator(*self.get_locator(), self.wait_timeout)


class WaitElementToBeClickable(Wait):
    short_name="wait_element_to_be_clickable"

    def execute(self):
        self.base_wait.wait_for_element_to_be_clickable(*self.get_locator(), self.wait_timeout)


class WaitStanleness(Wait):
    short_name="wait_staleness_of"

    def execute(self):
        web_element = self._driver.find_element(*self.get_locator())
        self.base_wait.wait_for_staleness_of(web_element, self.wait_timeout)


class WaitElementToBeSelected(Wait):
    short_name="wait_element_to_be_selected"

    def execute(self):
        self.base_wait.wait_for_elemente_to_be_selected_locstor(*self.get_locator(), self.wait_timeout)

class WaitElementSelectionToBeState(Wait):
    short_name="wait_element_selection_to_be_state"

    def execute(self):
        self.base_wait.wait_for_element_selection_to_be_state_locator(*self.get_locator(), self.wait_timeout)

class WaitForNumberOfWindowsToBe(Wait):
    short_name="wait_for_number_of_windows_to_be"

    def execute(self):
        self.base_wait.wait_for_number_of_windows_to_be(int(self.text_value), self.wait_timeout)

class WaitNewWindowIsOpened(Wait):
    short_name="wait_new_window_is_opened"

    def execute(self):
        self.base_wait.wait_for_new_window_is_opened(self._driver.current_window_handle(), self.wait_timeout)

class WaitAlertIsPresent(Wait):
    short_name="wait_alert_is_present"

    def execute(self):
        self.base_wait.wait_alert_is_present(self.wait_timeout)
"""
