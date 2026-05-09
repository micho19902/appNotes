FROM python:3.14.4

WORKDIR /app

# ARG NODE_VERSION=20.x

# # Instala Node.js (necesario para el frontend de Reflex)
# RUN apt-get update && apt-get install -y \
#     curl \
#     gnupg \
#     unzip \
#     procps \
#     && curl -fsSL https://deb.nodesource.com/setup_${NODE_VERSION} | bash - \
#     && apt-get install -y nodejs \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# # Crea un usuario no root para seguridad
# RUN adduser --disabled-password --home /app reflex
# RUN python -m venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Copia y da permisos
COPY  . /app
# RUN chown -R reflex:reflex /app
# USER reflex

# Instala dependencias e inicializa Reflex
RUN pip install --no-cache-dir -r requirements.txt
RUN reflex init

# Variables de entorno y puertos
ENV DATABASE_URL=''
ENV REFLEX_PORT=8000
ENV PORT=3000
EXPOSE 3000
EXPOSE 8000

# Healthcheck para que Railway sepa que tu app está viva
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8000/api/health || exit 1

STOPSIGNAL SIGKILL

# ¡El comando final!
CMD ["reflex", "run", "--env", "prod"]