from common.base_waits import BaseWait

from Domain.step import Step


class Wait(Step):
    short_name = "wait"

    def __init__(self, flow_id, args):
        super().__init__(flow_id)
        self.selector_type = self.get_selector(args["selector_type"])
        self.path_element = args["path_element"]
        self.wait_timeout = args["wait_timeout"]
        self.text_value = args["text_value"]
        self.state_type = args["state_type"]
        self._driver = self.get_driver_execution(flow_id)
        self.base_wait = BaseWait(self._driver)

    def get_locator(self):
        return (self.selector_type, self.path_element)


class WaitTitleIs(Wait):
    short_name = "wait_title_is"

    def execute(self):
        self.base_wait.wait_for_title_is(self.text_value, self.wait_timeout)
        return self.flow_id, None


class WaitTitleContains(Wait):
    short_name = "wait_title_contains"

    def execute(self):
        self.base_wait.wait_for_title_contains(self.text_value, self.wait_timeout)
        return self.flow_id, None


class WaitElementIsPresence(Wait):
    short_name = "wait_element_is_presence"

    def execute(self):
        self.base_wait.wait_for_element_is_presence(self.get_locator(), self.wait_timeout)
        return self.flow_id, None


class WaitUrlContains(Wait):
    short_name = "wait_url_contains"

    def execute(self):
        self.base_wait.wait_for_url_contains(self.text_value, self.wait_timeout)
        return self.flow_id, None


class WaitUrlMatches(Wait):
    short_name = "wait_url_matches"

    def execute(self):
        self.base_wait.wait_for_url_matches(self.text_value, self.wait_timeout)
        return self.flow_id, None


class WaitUrlChanges(Wait):
    short_name = "wait_url_changes"

    def execute(self):
        self.base_wait.wait_for_url_changes(self.text_value, self.wait_timeout)
        return self.flow_id, None


class WaitUrlToBe(Wait):
    short_name = "wait_url_to_be"

    def execute(self):
        self.base_wait.wait_for_url_to_be(self.text_value, self.wait_timeout)
        return self.flow_id, None


class WaitElementToBeVisible(Wait):
    short_name = "wait_element_to_be_visible"

    def execute(self):
        self.base_wait.wait_for_element_to_be_visible_locator(*self.get_locator(), self.wait_timeout)
        return self.flow_id, None


class WaitAllElementsIsPresence(Wait):
    short_name = "wait_all_elements_is_presence"

    def execute(self):
        self.base_wait.wait_for_all_elements_is_presence(*self.get_locator(), self.wait_timeout)
        return self.flow_id, None


class WaitAnyElementToBeVisible(Wait):
    short_name = "wait_any_element_to_be_visible"

    def execute(self):
        self.base_wait.wait_for_any_element_to_be_visible_locator(*self.get_locator(), self.wait_timeout)
        return self.flow_id, None


class WaitAllElementsToBeVisible(Wait):
    short_name = "wait_all_elements_to_be_visible"

    def execute(self):
        self.base_wait.wait_for_all_elements_to_be_visible_locator(*self.get_locator(), self.wait_timeout)
        return self.flow_id, None


class WaitElementToBeTextIsPresent(Wait):
    short_name = "wait_element_to_be_text_is_present"

    def execute(self):
        self.base_wait.wait_for_element_to_be_text_is_present(*self.get_locator(), self.wait_timeout)
        return self.flow_id, None


class WaitElementTextValueIsPresent(Wait):
    short_name = "wait_element_text_value_is_present"

    def execute(self):
        self.base_wait.wait_for_element_text_value_is_present(*self.get_locator(), self.wait_timeout)
        return self.flow_id, None


class WaitFrameToBeAvailableAndSwitchToIt(Wait):
    short_name = "wait_frame_to_be_available_and_switch_to_it"

    def execute(self):
        self.base_wait.wait_for_frame_to_be_available_and_switch_to_it(*self.get_locator(), self.wait_timeout)
        return self.flow_id, None


class WaitElementToBeInvisible(Wait):
    short_name = "wait_element_to_be_invisible"

    def execute(self):
        self.base_wait.wait_for_element_to_be_invisibe_locator(*self.get_locator(), self.wait_timeout)
        return self.flow_id, None


class WaitElementToBeClickable(Wait):
    short_name = "wait_element_to_be_clickable"

    def execute(self):
        self.base_wait.wait_for_element_to_be_clickable(*self.get_locator(), self.wait_timeout)
        return self.flow_id, None


class WaitStanleness(Wait):
    short_name = "wait_staleness_of"

    def execute(self):
        web_element = self._driver.find_element(*self.get_locator())
        self.base_wait.wait_for_staleness_of(web_element, self.wait_timeout)
        return self.flow_id, None


class WaitElementToBeSelected(Wait):
    short_name = "wait_element_to_be_selected"

    def execute(self):
        self.base_wait.wait_for_elemente_to_be_selected_locstor(*self.get_locator(), self.wait_timeout)
        return self.flow_id, None


class WaitElementSelectionToBeState(Wait):
    short_name = "wait_element_selection_to_be_state"

    def execute(self):
        self.base_wait.wait_for_element_selection_to_be_state_locator(*self.get_locator(), self.wait_timeout)
        return self.flow_id, None


class WaitForNumberOfWindowsToBe(Wait):
    short_name = "wait_for_number_of_windows_to_be"

    def execute(self):
        self.base_wait.wait_for_number_of_windows_to_be(int(self.text_value), self.wait_timeout)
        return self.flow_id, None


class WaitNewWindowIsOpened(Wait):
    short_name = "wait_new_window_is_opened"

    def execute(self):
        self.base_wait.wait_for_new_window_is_opened(self._driver.current_window_handle(), self.wait_timeout)
        return self.flow_id, None


class WaitAlertIsPresent(Wait):
    short_name = "wait_alert_is_present"

    def execute(self):
        self.base_wait.wait_alert_is_present(self.wait_timeout)
        return self.flow_id, None
