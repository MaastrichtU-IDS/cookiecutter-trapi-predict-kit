FROM python:3.8

LABEL org.opencontainers.image.source="https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_name}}"

# Change the current user to root and the working directory to /app
USER root
WORKDIR /app

RUN apt-get update && \
    # apt-get install -y build-essential wget curl && \
    pip install --upgrade pip

COPY . .

RUN pip install -e ".[train,test,dev]"

RUN dvc pull -f

CMD [ "python", "src/{{cookiecutter.module_name}}/train.py", "train-model" ]