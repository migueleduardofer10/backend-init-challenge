FROM python:3.13-slim

# Evita buffering y pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /src

# Dependencias del sistema (para psycopg2)
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente
COPY src/ /src/
COPY tests/ /tests/ 

# Puerto expuesto
EXPOSE 8000

# Arranca FastAPI (el paquete raíz es "app", porque está en /src/app)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
