from web_services.ws_core import WsCore


def test_open_browser(endpoint_flow):
    body = {
        "command": "open_browser",
        "arguments": {"browser": "firefox",
                      "url": "http://www.python.org",
                      "window_state": "Maximizado",
                      "wait_timeout": "30",
                      "headless": "False",
                      "browser_instance": "driver"},
        "flow_id": 0,
        "variable_data": "driver"
    }
    response = WsCore.execute_request_post(endpoint=endpoint_flow, json=body)
    assert response.status_code == 200

