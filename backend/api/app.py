# app.py
import sqlite3
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel

app = FastAPI()

# --- Modelos de Datos con Pydantic ---
# Modelo para la validación de datos en el endpoint POST /form
class FormInput(BaseModel):
    username: str
    comment: str

# --- Endpoints de la API ---

# 1. Endpoint GET /: Devuelve una página HTML estática
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("api/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

# 2. Endpoint GET /data: Simula una lectura de base de datos
@app.get("/data")
async def get_data():
    try:
        conn = sqlite3.connect('test.db')
        conn.row_factory = sqlite3.Row # Para obtener resultados como diccionarios
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, description FROM items")
        items = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return {"data": items}
    except Exception as e:
        # En otro contexto se podria registrar el error
        raise HTTPException(status_code=500, detail="Error interno al acceder a la base de datos.")

# 3. Endpoint POST /form: Simula la recepción y validación de un formulario
@app.post("/form")
async def submit_form(form_data: FormInput):
    # Validación sencilla (Pydantic ya se encarga de que los campos existan y sean strings)
    if not form_data.username or not form_data.comment:
        raise HTTPException(status_code=400, detail="Los campos 'username' y 'comment' no pueden estar vacíos.")
    
    # Lógica de negocio simulada
    print(f"Formulario recibido de {form_data.username}: {form_data.comment}")
    
    return {"status": "éxito", "message": "Formulario recibido correctamente."}

# 4. Endpoint GET /redirect: Realiza una redirección HTTP
@app.get("/redirect")
async def redirect_to_home():
    return RedirectResponse(url="/")