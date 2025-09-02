# Backend Init 🚀

Este proyecto implementa un **backend modular** con **Arquitectura Hexagonal**, **CQRS** y **bundle-contexts**, usando **FastAPI**, **SQLAlchemy** y **RabbitMQ**.

---

## 📌 Comenzando

Estas instrucciones te permitirán obtener una copia del proyecto en tu máquina local para desarrollo y pruebas.

### Pre-requisitos 📋

Necesitas instalar y tener configurados:

```bash
Docker
Docker Compose
Python 3.13 (opcional, si quieres ejecutar fuera de Docker)
```

---

## 🔧 Instalación

Clona el repositorio y entra en el directorio del proyecto:

```bash
git clone <repo_url>
cd backend-init
```

Construye y levanta los servicios:

```bash
docker compose up --build
```

Esto levantará:

- **Postgres** (Base de datos)
- **RabbitMQ** (Broker de mensajería)
- **App** (FastAPI)
- **Worker** (Consumidor de comandos)

---

## ▶️ Uso

La API quedará disponible en:

```
http://localhost:8000
```

Puedes probar los endpoints con Swagger UI:

```
http://localhost:8000/docs
```

### Ejemplo: Crear usuario

```http
POST /users
Content-Type: application/json

{
  "name": "Ana",
  "email": "ana@test.com",
  "password": "StrongPass1"
}
```

Respuesta esperada:

```json
{
  "status_code": 200,
  "message": "User command published",
  "data": null
}
```

### Ejemplo: Consultar usuario

```http
GET /users/1
```

Respuesta esperada:

```json
{
  "status_code": 200,
  "message": "Success",
  "data": {
    "id": 1,
    "name": "Ana",
    "email": "ana@test.com",
    "status": "ACTIVE"
  }
}
```

---

## 🧪 Pruebas

Ejecuta las pruebas unitarias e integración con:

```bash
docker compose run --rm app pytest /tests --cov=modules/users/domain --cov-report=term-missing
```

Esto ejecuta todos los tests y muestra la cobertura del **dominio**, la cual debe ser ≥ 80% ✅.

---

## 📂 Estructura del Proyecto

```text
src/
├── app/                  # Entrypoint FastAPI
├── core/                 # Config, contenedor DI, base
├── modules/
│   └── users/            # Contexto Users (Dominio, Aplicación, Infraestructura)
│   └── auth/             # Contexto Auth (placeholder)
tests/                    # Pruebas unitarias e integración
```

---

## 🏗️ Arquitectura

- **Hexagonal Architecture**: el dominio no depende de infraestructura.
- **CQRS**: separación entre **commands** (RabbitMQ) y **queries** (lectura directa).
- **Bundle-contexts**: contexts lógicos (`users`, `auth`) agrupados en módulos.

---

## 🐳 Docker

### Levantar servicios

```bash
docker compose up --build
```

### Ver logs en tiempo real

```bash
docker compose logs -f
```

### Ejecutar worker manualmente

```bash
docker compose run --rm worker
```

---

## 📖 Decisiones Arquitectónicas

1. **Dominio puro**: entidades y reglas sin dependencias externas.
2. **Infraestructura desacoplada**: adaptadores para DB y RabbitMQ.
3. **CQRS estricto**: comandos no retornan datos, consultas no modifican estado.
4. **Escalabilidad**: fácil agregar nuevos contexts (`billing`, `notifications`, etc.).

