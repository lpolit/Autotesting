from web_services.ws_core import WsCore

endpoint = "http://localhost:5000/flow"

def test_send_keys(endpoint_flow):
    body = {
        "comando": "send_keys",
        "argumentos": { "selector_type": "xpath",
                        "path_element": "//*[@id='F1:username']",
                        "text_to_send": "20324037056",
                        "wait_timeout": "10"
                       },
        "flow_id": 1
    }

    response = WsCore.execute_request_post(endpoint=endpoint_flow, json=body)
    assert response.status_code == 200
