# Dockerfile

# 1. Imagen base liviana
FROM python:3.9-slim

# 2. Directorio de trabajo
WORKDIR /app

# 3. Copiar dependencias primero
COPY requirements.txt .

# 4. Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar todo el código fuente
COPY . .

# 6. Exponer puerto para Gunicorn
EXPOSE 8000

# 7. Comando de inicio: ejecutar setup_db.py y luego iniciar Gunicorn
CMD ["sh", "-c", "python db/setup_db.py && gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 api.app:app"]
