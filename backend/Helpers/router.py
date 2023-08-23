import importlib
from os import listdir

import Domain

router_command = {}


def set_router_command():

    for mod in listdir(Domain.__path__[0]):
        modul=importlib.import_module("Domain." + mod.replace(".py", ""))
        for nombre in dir(modul):
            objeto = getattr(modul, nombre)
            if callable(objeto):
                if isinstance(objeto, type):
                    try:
                        router_command[objeto.short_name] = objeto
                    except:
                        continue
    return router_command
