from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseWait:

    def __init__(self, driver):
        self.driver = driver

    def wait_for(self, condition, timeout=10):
        WebDriverWait(self.driver, timeout).until(condition)

    def wait_for_title_is(self, title, timeout=10):
        self.wait_for(ec.title_is(title), timeout)

    def wait_for_title_contains(self, title, timeout=10):
        self.wait_for(ec.title_contains(title), timeout)

    def wait_for_element_is_presence(self, locator, timeout=10):
        self.wait_for(ec.presence_of_element_located(locator), timeout)

    def wait_for_url_contains(self, url, timeout=10):
        self.wait_for(ec.url_contains(url), timeout)

    def wait_for_url_matches(self, pattern, timeout=10):
        self.wait_for(ec.url_matches(pattern), timeout)

    def wait_for_url_changes(self, url, timeout=10):
        self.wait_for(ec.url_changes(url), timeout)

    def wait_for_url_to_be(self, url, timeout=10):
        self.wait_for(ec.url_to_be(url), timeout)

    def wait_for_element_to_be_visible(self, elem, timeout=10):
        self.wait_for(ec.visibility_of(elem), timeout)

    def wait_for_element_to_be_visible_locator(self, locator, timeout=10):
        self.wait_for(ec.visibility_of_element_located(locator), timeout)

    def wait_for_all_elements_is_presence(self, locator, timeout=10):
        self.wait_for(ec.presence_of_all_elements_located(locator), timeout)

    def wait_for_any_element_to_be_visible_locator(self, locator, timeout=10):
        self.wait_for(ec.visibility_of_any_elements_located(locator), timeout)

    def wait_for_all_elements_to_be_visible_locator(self, locator, timeout=10):
        self.wait_for(ec.visibility_of_all_elements_located(locator), timeout)

    def wait_for_element_to_be_text_is_present(self, locator, text, timeout=10):
        self.wait_for(ec.text_to_be_present_in_element(locator, text), timeout)

    def wait_for_element_text_value_is_present(self, locator, text, timeout=10):
        self.wait_for(ec.text_to_be_present_in_element_value(locator, text), timeout)

    def wait_for_frame_to_be_available_and_switch_to_it(self, locator, timeout=10):
        self.wait_for(ec.frame_to_be_available_and_switch_to_it(locator), timeout)

    def wait_for_element_to_be_invisibe(self, element, timeout=10):
        self.wait_for(ec.invisibility_of_element_located(element), timeout)

    def wait_for_element_to_be_invisibe_locator(self, locator, timeout=10):
        self.wait_for(ec.invisibility_of_element(locator), timeout)

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        self.wait_for(ec.element_to_be_clickable(locator), timeout)

    def wait_for_staleness_of(self, element, timeout=10):
        self.wait_for(ec.staleness_of(element), timeout)

    def wait_for_elemente_to_be_selected(self, element, timeout=10):
        self.wait_for(ec.element_to_be_selected(element), timeout)

    def wait_for_elemente_to_be_selected_locstor(self, locator, timeout=10):
        self.wait_for(ec.element_located_to_be_selected(locator), timeout)

    def wait_for_element_selection_to_be_state(self, element, is_selected, timeout=10):
        self.wait_for(ec.element_selection_state_to_be(element, is_selected), timeout)

    def wait_for_element_selection_to_be_state_locator(self, locator, is_selected, timeout=10):
        self.wait_for(ec.element_located_selection_state_to_be(locator, is_selected), timeout)

    def wait_for_number_of_windows_to_be(self, number_of_window, timeout=10):
        self.wait_for(ec.number_of_windows_to_be(number_of_window), timeout)

    def wait_for_new_window_is_opened(self, current_handles, timeout=10):
        self.wait_for(ec.new_window_is_opened(current_handles), timeout)

    def wait_alert_is_present(self, timeout=10):
        self.wait_for(ec.alert_is_present(), timeout)
