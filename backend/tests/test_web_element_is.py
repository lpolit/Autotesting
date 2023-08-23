from web_services.ws_core import WsCore


def test_assert_we_is_visible(endpoint_flow, selector="xpath", path="//*[@id='F1:username']"):

    body = {
        "comando": "assert_is_visible",
        "argumentos": { "selector_type": selector,
                        "path_element": path,
                       },
        "flow_id": 1
    }
    response = WsCore.execute_request_post(endpoint=endpoint_flow, json=body)
    assert response.status_code == 200

def test_assert_we_is_enabled(endpoint_flow, selector="xpath", path="//*[@id='F1:username']"):
    body = {
        "comando": "assert_is_enabled",
        "argumentos": { "selector_type": selector,
                        "path_element": path,
                       },
        "flow_id": 1
    }
    response = WsCore.execute_request_post(endpoint=endpoint_flow, json=body)
    assert response.status_code == 200


def test_assert_we_is_selected(endpoint_flow, selector="xpath", path="//*[@id='F1:username']"):
    body = {
        "comando": "assert_is_selected",
        "argumentos": { "selector_type": selector,
                        "path_element": path,
                       },
        "flow_id": 1
    }
    response = WsCore.execute_request_post(endpoint=endpoint_flow, json=body)
    assert response.status_code == 200

