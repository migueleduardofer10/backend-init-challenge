FROM python:3.13-slim

## Evita buffering y crea directorio
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crea directorio de trabajo
WORKDIR /app

# Dependencias del sistema (psycopg2)
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Instala requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código explícitamente
COPY main.py /app/main.py
COPY app/ /app/app/

# Puerto de la app
EXPOSE 8000

# Por defecto levantamos la API ()
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
