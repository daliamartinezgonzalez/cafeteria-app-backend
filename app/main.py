from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session

from app.database import get_db
from models.usuario import Usuario
from schemas.usuario import UsuarioResponse
from models.rol import Rol
from models.permiso import Permiso
from models.rol_permiso import RolPermiso
from routers.usuarios import router as usuarios_router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routers.auth import router as auth_router

app = FastAPI()
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errores = []

    mensajes = {
        "missing": "Este campo es obligatorio",
        "string_too_short": "El texto es demasiado corto",
        "string_too_long": "El texto supera la cantidad máxima de caracteres",
        "value_error": "El valor ingresado no es válido",
        "int_parsing": "Este campo debe ser un número entero",
        "bool_parsing": "Selecciona un valor válido",
    }

    for error in exc.errors():
        campo = error["loc"][-1]
        tipo = error["type"]

        mensaje = mensajes.get(tipo, "El dato ingresado no es válido")

        if tipo == "string_too_short":
            mensaje = f"Debe tener al menos {error['ctx']['min_length']} caracteres"

        elif tipo == "string_too_long":
            mensaje = f"No debe superar los {error['ctx']['max_length']} caracteres"

        errores.append({
            "campo": campo,
            "mensaje": mensaje
        })

    return JSONResponse(
        status_code=422,
        content={
            "mensaje": "Hay errores en los datos enviados",
            "errores": errores
        }
    )
app.include_router(usuarios_router)
app.include_router(auth_router)