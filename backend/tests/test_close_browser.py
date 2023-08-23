from web_services.ws_core import WsCore

def test_close_browser(endpoint_flow):
    body = {
        "comando": "close_browser",
        "argumentos": {},
        "flow_id": 1
    }

    response = WsCore.execute_request_post(endpoint=endpoint_flow, json=body)
    assert response.status_code == 200
