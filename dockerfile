FROM python:3.12-slim

# Instala dependencias del sistema
RUN apt-get update && \
    apt-get install -y \
    git \
    curl \
    unzip \
    jq \
    zip \
    groff \
    less \
    && rm -rf /var/lib/apt/lists/*

# Instala AWS CLI v2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

# Instala AWS SAM CLI
RUN pip install --upgrade aws-sam-cli

# Verificaciones opcionales
RUN aws --version && \
    sam --version && \
    python --version && \
    jq --version && \
    git --version

ENTRYPOINT [ "bash" ]