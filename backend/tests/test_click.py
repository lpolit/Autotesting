from web_services.ws_core import WsCore

def test_click_left(endpoint_flow):
    body = {
        "comando": "click_left",
        "argumentos": { "selector_type": "xpath",
                        "path_element": "//*[@id='F1:username']",
                        "click_type": "click_left",
                        "wait_timeout":"10"
                       },
        "flow_id": 1
    }

    response = WsCore.execute_request_post(endpoint=endpoint_flow, json=body)
    assert response.status_code == 200
