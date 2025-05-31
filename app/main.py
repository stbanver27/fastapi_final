from fastapi import FastAPI
from app.routers.usuarios import router as usuarios_router


app = FastAPI(
    title= "API de gestión de usuarios",
    version= "1.0.0",
    description= "API para gestionar usuarios"
)

#Traeremos los de las rutas (routers)
app.include_router(usuarios_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API"}