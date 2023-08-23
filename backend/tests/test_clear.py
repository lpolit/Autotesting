from web_services.ws_core import WsCore

def test_clear(endpoint_flow):
    body = {
        "comando": "clear",
        "argumentos": { "selector_type": "xpath",
                        "path_element": "//*[@id='F1:username']",
                        "wait_timeout":"10"
                       },
        "flow_id": 1
    }

    response = WsCore.execute_request_post(endpoint=endpoint_flow, json=body)
    assert response.status_code == 200
