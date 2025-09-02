# --- Imagen base ---
FROM python:3.13-slim

# --- Configuración de Python ---
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# --- Directorio de trabajo ---
WORKDIR /src

# --- Dependencias del sistema (para psycopg2) ---
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# --- Instalar dependencias Python ---
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Copiar código fuente y tests ---
COPY src/ /src/
COPY tests/ /tests/ 

# --- Exponer puerto ---
EXPOSE 8000

# --- Comando de arranque ---
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
