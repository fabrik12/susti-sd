# Documentación Técnica: Sistema de Backend con Múltiples Proxy Inversos

## 1. Descripción General

Este proyecto implementa un sistema backend que demuestra el uso de diferentes servidores proxy inversos (Apache, Nginx y Traefik) para gestionar el tráfico hacia una API FastAPI.

## 2. Arquitectura del Sistema

### 2.1 Componentes Principales

- **API Backend (FastAPI)**
  - Puerto: 8000
  - Proporciona endpoints REST
  - Incluye gestión de base de datos SQLite
- **Proxies Inversos**
  - Apache HTTP Server 2.4
  - Nginx
  - Traefik v2.11

### 2.2 Estructura del Proyecto

```
backend/
├── api/
│   ├── app.py          # API principal
│   └── index.html      # Página de inicio
├── db/
│   └── setup_db.py     # Configuración de BD
├── docker-compose-*.yml # Configuraciones Docker
├── Dockerfile          # Construcción de imagen API
└── *.conf              # Archivos configuración proxies
```

## 3. API Endpoints

| Endpoint    | Método | Descripción                   |
| ----------- | ------ | ----------------------------- |
| `/`         | GET    | Página de inicio HTML         |
| `/data`     | GET    | Obtiene datos de la BD SQLite |
| `/form`     | POST   | Procesa datos de formulario   |
| `/redirect` | GET    | Redirecciona a inicio         |

## 4. Configuraciones de Proxy

### 4.1 Nginx

```nginx
location / {
    proxy_pass http://backend-api:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

### 4.2 Apache

```apache
ProxyPass        "/" "http://backend-api:8000/"
ProxyPassReverse "/" "http://backend-api:8000/"
```

### 4.3 Traefik

```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.fastapi.rule=Host(`localhost`)"
  - "traefik.http.services.fastapi.loadbalancer.server.port=8000"
```

## 5. Instrucciones de Despliegue

### 5.1 Con Nginx

```bash
docker-compose -f docker-compose-nginx.yml up
```

### 5.2 Con Apache

```bash
docker-compose -f docker-compose-apache.yml up
```

### 5.3 Con Traefik

```bash
docker-compose -f docker-compose-traefik.yml up
```

## 6. Requisitos del Sistema

- Docker Engine
- Docker Compose
- Python 3.9+
- Dependencias listadas en requirements.txt

## 7. Consideraciones de Seguridad

- Configuración de encabezados HTTP seguros
- Sin exposición directa del puerto de la API
- Validación de datos con Pydantic
- Manejo de errores HTTP apropiado

## 8. Monitoreo y Logs

- Logs de acceso estándar de los servidores proxy
- Logs de la aplicación FastAPI
- Dashboard de Traefik (puerto 8080)

## 9. Mantenimiento

### 9.1 Base de Datos

- La base de datos SQLite se inicializa automáticamente
- Los datos de ejemplo se cargan en cada inicio

### 9.2 Actualizaciones

- Las imágenes base usan tags específicos para control de versiones
- Configuraciones modulares para fácil actualización

## 10. Limitaciones Conocidas

- SQLite para desarrollo/pruebas
- Sin configuración SSL/TLS
- Sin autenticación implementada
