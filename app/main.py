from fastapi import FastAPI

app = FastAPI(
    title= "API de gestión de usuarios",
    version= "1.0.0",
    description= "API para gestionar usuarios"
)

#Traeremos los de las rutas (routers)
