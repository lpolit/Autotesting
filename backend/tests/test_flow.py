import time

from tests.test_clear import test_clear
from tests.test_click import test_click_left
from tests.test_close_browser import test_close_browser
from tests.test_get_text import test_get_text
from tests.test_get_web_element import test_get_web_element
from tests.test_open_browser import test_open_browser
from tests.test_send_keys import test_send_keys
from tests.test_wait import *
from tests.test_web_element_is import *





def test_flow(endpoint_flow):
    test_open_browser(endpoint_flow)
    test_click_left(endpoint_flow)
    test_send_keys(endpoint_flow)
    # test_assert_we_is_visible(endpoint_flow)
    # test_assert_we_is_enabled(endpoint_flow)
    # #test_assert_we_is_selected(endpoint_flow)
    # test_wait_title_is(endpoint_flow)
    # test_wait_title_contains(endpoint_flow)
    # test_wait_element_is_presence(endpoint_flow)
    # test_wait_url_contains(endpoint_flow)
    # #Falta crear los test de todas esperas
    test_get_text(endpoint_flow)
    test_get_web_element(endpoint_flow)
    test_clear(endpoint_flow)
    test_close_browser(endpoint_flow)








