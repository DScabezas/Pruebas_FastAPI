from fastapi import FastAPI
from sqlmodel import SQLModel

application = FastAPI()

class Usuario(SQLModel):
    id: int
    nombre: str
    password: str

usuarios = [Usuario(id=1, nombre="Juan", password="1234"),]

@application.get("/")
def root():
    return {"message": "Hello world"}

@application.get("/user")
def obtener_usuarios():
    return usuarios

@application.get("/user/{id}")
def obtener_usuario_id(id: int):    
    for usuario in usuarios:
        if usuario.id == id:
            return usuario
        else:
            return {"message":f"Usuario con id = {id} no existe"}

@application.delete("/users/{id}")
def borrar_usuario(id: int):
    for usuario in usuarios:
        if usuario.id == id:
            usuarios.remove(usuario)
            return {"message":f"Usuario con id = {id} ha sido eliminado"}
        else:
            return {"message":f"Usuario con id = {id} no existe"}

@application.post("/users")
def crear_usuario(usuario: Usuario):
    numero_usuarios = len(usuarios)
    usuario.id = numero_usuarios + 1
    usuarios.append(usuario)
    return {"message": "Usuario Creado"}
