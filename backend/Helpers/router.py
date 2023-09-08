import importlib
from os import listdir

import domain

router_command = {}


def set_router_command():

    for mod in listdir(domain.__path__[0]):
        modul=importlib.import_module("domain." + mod.replace(".py", ""))
        for nombre in dir(modul):
            objeto = getattr(modul, nombre)
            if callable(objeto):
                if isinstance(objeto, type):
                    try:
                        router_command[objeto.short_name] = objeto
                    except:
                        continue
    return router_command
