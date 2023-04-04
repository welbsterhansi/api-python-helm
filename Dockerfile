FROM python:3.10.9-alpine

WORKDIR /code

# Copiar requirements.txt para o diretório de trabalho
COPY ./app/requirements.txt /code/requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copiar todo o conteúdo da pasta app para o diretório de trabalho
COPY ./app /code

# Expor a porta 80
EXPOSE 80

# Iniciar o servidor usando o Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
