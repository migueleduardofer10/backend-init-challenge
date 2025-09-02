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
├── app/                        # Entrypoint FastAPI
├── core/                       # Config, contenedor DI, base
├── modules/
│   ├── users/                  # Contexto Users (Dominio, Aplicación, Infraestructura)
│   │   ├── application/        # Commands, Queries, DTOs, Mappers
│   │   ├── domain/             # Entities, ValueObjects, Specs, Policies, Ports, Errors
│   │   └── infrastructure/     # Repositories, Schemas, Adapters (RabbitMQ, DB, etc.)
│   └── auth/                   # Contexto Auth (placeholder)
tests/
├── unit/                       # Pruebas unitarias (domain, application)
└── integration/                # Pruebas de integración (infraestructura, API)
```
  - `src/`: código productivo.
    - `app/`: puntos de entrada (FastAPI, routers HTTP).
    - `core/`: configuración transversal (DB, contenedor DI, responses).
    - `modules/`: contexts (users, auth) organizados en domain / application / infrastructure.
  - `tests/`: pruebas unitarias e integración.
    - `unit/`: tests de dominio y aplicación aislados.
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
5. **Inyección de dependencias**: centralizada en `core/container.py` con `dependency-injector`.
6. **DTOs y Mappers**: evitan exponer entidades directamente y aíslan el dominio de la capa de transporte.
7. **Manejo de errores**: excepciones de dominio claras (ej. `UserNotFoundError`, `PasswordPolicyError`).
8. **Pruebas dirigidas al dominio**: cobertura ≥80% para garantizar reglas de negocio robustas.
9. **Seguridad básica**: contraseñas almacenadas con hash seguro (bcrypt).
10. **Mensajería asíncrona**: RabbitMQ permite desacoplar commands y dar resiliencia.

