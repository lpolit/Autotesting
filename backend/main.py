from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from starlette import status

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from Helpers.router import set_router_command, router_command

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)
plani = {}


######## MODEL ###########
class Comando(BaseModel):
    command: str
    arguments: Optional[dict]
    flow_id: Optional[int]
    variable_data: Optional[object]


############### ENDPOINTS ###################
@app.get("/")
async def root():
    pass
    return {"message": "Hello World"}


@app.post("/flow")
def flow(comando: Comando):
    try:
        step = router_command[comando.command](comando.flow_id, comando.arguments)
        comando.flow_id, comando.variable_data = step.execute()
        return comando
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: {e}",
        )

@app.get("/test")
def flow():
    return {"HOLAAAAAAAAAAAAAAA"}

# @app.post("/demo")
# async def demo():
#     flow_id=abrir_browser(opt={"browser":"chrome","url":"https://authhomo.afip.gob.ar/contribuyente_/login.xhtml","headless":False})
#     _driver = plani[flow_id]
#     click(flow_id, opt={"xpath": "//*[@id='F1:username']", "tipo": "izquierdo"})
#     enviar_texto(flow_id, opt={"xpath":"//*[@id='F1:username']","texto":"20324037056"})
#     click(flow_id, opt={"xpath": "//*[@id='F1:btnSiguiente']", "tipo": "izquierdo"})
#     enviar_texto(flow_id, opt={"xpath":"//*[@id='F1:password']","texto":"Afip123456!"})
#     click(flow_id, opt={"xpath": "//*[@id='F1:btnIngresar']", "tipo": "izquierdo"})
#     click(flow_id, opt={"xpath": "//span[text()=' Mis Servicios']", "tipo": "izquierdo"})
#     click(flow_id, opt={"xpath": "//div[@title='rcel']//h4", "tipo": "izquierdo"})
#     esperar_a(flow_id,opt={"nro_ventanas":2})
#     cambiar_ventana(flow_id, opt={"titulo":"RCEL"})
#     click(flow_id, opt={"xpath": "//input[@value='20040831615-VGEPRUP GGAUI']", "tipo": "izquierdo"})
#     click(flow_id, opt={"xpath": "//*[@id='btn_consultas']", "tipo": "izquierdo"})
#     limpiar_campo(flow_id, opt={"xpath":"//*[@id='fed']"})
#     enviar_texto(flow_id, opt={"xpath":"//*[@id='fed']","texto":"01/01/2021"})
#     click(flow_id, opt={"xpath": "//option[@value='11']", "tipo": "izquierdo"})
#     click(flow_id, opt={"xpath": "//input[@value='Buscar']", "tipo": "izquierdo"})
#     verificar_existencia(flow_id,opt={"xpath":"//table[@class='jig_table']"})
#     cerrar_browser(flow_id)
#     return {"Flux finalizado OK"}


if __name__ == "__main__":
    set_router_command()
    uvicorn.run("main:app", port=5000, log_level="info")
