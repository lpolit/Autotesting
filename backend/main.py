from typing import Optional

from fastapi import FastAPI, HTTPException, Body, Depends
from pydantic import BaseModel, Field, EmailStr
import uvicorn
from starlette import status

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from Helpers.router import set_router_command, router_command
from auth.jwt_handler import signJWT
from auth.jwt_bearer import jwtBearer
import db.user_db as userDb
import db.flux_db as fluxDb
import db.project_db as projectDb

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

class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
           "user_demo":{
               "name":"leogg",
               "email":"leoggg@gmail.com",
               "pass": "123"
           }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        the_schema = {
           "user_demo":{
               "email":"leoggg@gmail.com",
               "pass": "123"
           }
        }

class FluxSchema(BaseModel):
    flux_name: str
    date: str
    state: str
    flux: str
    user: str
    project_id: str

class ProjectSchema(BaseModel):
    project_name: str
    date: str
    state: str
    user: str


############### ENDPOINTS ###################

@app.get("/")
async def root():
    pass
    return {"message": "Hello World"}

### PROJECT SERVICE ###
@app.post("/project/insert")
def insert_project(project: ProjectSchema):
    try:
        id_project = projectDb.insert_project(project)
        return id_project
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: {e}",
        )

@app.post("/project/update/{project_id}")
def update_project(project_id: str, project: ProjectSchema):
    try:
        id_project = projectDb.update_project(project, int(project_id))
        return id_project
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: {e}",
        )


@app.post("/project/getAll")
def get_all_projects():
    try:
        projects = projectDb.get_all_projects()
        return projects
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: {e}",
        )

@app.post("/project/getAll/{username}")
def get_projects_user_name(username: str):
    try:
        projects = projectDb.get_all_projects_for_user(username)
        return projects
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: {e}",
        )



### FLOW SERVICE ########
@app.post("/flow/getAll/{project_id}")
def get_all_flow_from_project(project_id: str):
    try:
        flujos = fluxDb.get_fluxs_from_project(int(project_id))
        return flujos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: {e}",
        )
@app.post("/flow/getAll")
def get_all_flow():
    try:
        flujos = fluxDb.get_all_fluxs()
        return flujos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: {e}",
        )

@app.delete("/flow/deleteAll")
def flow():
    try:
        fluxDb.delete_all_flujos()
        return "Borrado Exitoso"
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: {e}",
        )

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

@app.post("/flow/save/{flow_id}")
def flow_update(flux: FluxSchema, flow_id: str):
    try:
        fluxDb.update_flux()(flux, flow_id)
        return "Guardado Exitoso"
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: {e}",
        )

@app.post("/flow/save")
def flow_insert(flux: FluxSchema):
    try:
        id_flux = fluxDb.insert_flux(flux)
        return id_flux;
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: {e}",
        )

@app.post("/flow/abrir")
def flow_abrir(flux: FluxSchema):
    try:
        flujo = fluxDb.get_flux(flux)
        return flujo[1]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: {e}",
        )



##### USER SERVICE #############

@app.post("/user/signup")
def user_signup(user : UserSchema = Body(default=None)):
    userDb.insert_user(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    users = userDb.get_all_users()
    for user in users:
        if user[1]==data.email and user[2] == data.password:
            return True
    return False

@app.post("/user/login")
def user_login(user : UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: Invalid login details!",
        )

@app.post("/user/getAll")
def get_all_users():
    try:
        users = userDb.get_all_users()
        return users
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: {e}",
        )

##### TEST SERVICE #####
@app.get("/test", dependencies=[Depends(jwtBearer())])
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
