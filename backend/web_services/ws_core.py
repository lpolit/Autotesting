import requests
from loguru import logger


def _log_input(method=None, endpoint=None, **kwargs):
    logger.info("################# REQUEST ########################")
    logger.info(f"Se ejecuta la API: {endpoint}")
    logger.debug("Se ejecuta la API con estos datos de entrada:")
    logger.debug(f"Método: {method}")
    logger.debug(f"Endpoint: {endpoint}")
    logger.debug(f"Argumentos: {kwargs}")


def _log_output(status_code=None, text=None):
    logger.debug("################# RESPONSE #####################")
    logger.debug("Es response de la API es:")
    logger.debug(f"Status code: {status_code}")
    logger.debug(f"Error message: {text}")


class WsCore:

    _status = {
        "OK": 200,
        "NOT_FOUND": 400,
        "UNAUTHORIZED": 401
    }

    @staticmethod
    def get_status(key):
        return WsCore._status[key]

    @staticmethod
    def execute_request(session=None, verify=False, endpoint=None, **kwargs):
        request = requests
        if session is not None:
            request = session

        _log_input(method='GET', endpoint=endpoint, **kwargs)
        response = request.get(endpoint, verify=verify, **kwargs)
        _log_output(status_code=response.status_code, text=response.text)
        return response

    @staticmethod
    def execute_request_post(session=None, endpoint=None, verify=False, **kwargs):
        request = requests
        if session is not None:
            request = session
        _log_input(method='POST', endpoint=endpoint, **kwargs)
        response = request.request('POST', endpoint, verify=verify, **kwargs)
        _log_output(status_code=response.status_code, text=response.text)
        return response

    @staticmethod
    def execute_request_put(session=None, endpoint=None, verify=False, **kwargs):
        request = requests
        if session is not None:
            request = session
        _log_input(method='PUT', endpoint=endpoint, **kwargs)
        response = request.put(endpoint, verify=verify, **kwargs)
        _log_output(status_code=response.status_code, text=response.text)
        return response

    @staticmethod
    def execute_request_delete(session=None, endpoint=None, verify=False, **kwargs):
        request = requests
        if session is not None:
            request = session
        _log_input(method='DELETE', endpoint=endpoint, **kwargs)
        response = request.delete(endpoint, verify=verify, **kwargs)
        _log_output(status_code=response.status_code, text=response.text)
        return response
