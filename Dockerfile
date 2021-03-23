FROM python:latest
USER root

RUN rm /etc/apt/sources.list && \
    echo "deb https://mirrors.cloud.tencent.com/debian buster main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb https://mirrors.cloud.tencent.com/debian buster-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src https://mirrors.cloud.tencent.com/debian buster main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src https://mirrors.cloud.tencent.com/debian buster-updates main contrib non-free" >> /etc/apt/sources.list

SHELL ["/bin/bash", "-c"]

USER root

RUN apt-get update
RUN apt-get install gcc -y

RUN pip install  --no-cache-dir poetry

WORKDIR /OmniDB
ADD ./pyproject.toml .
ADD ./poetry.lock . 

# Install dependecies in system
# RUN apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
RUN poetry config virtualenvs.create false && poetry install

ADD ./OmniDB/ ./
RUN sed -i "s/LISTENING_ADDRESS    = '127.0.0.1'/LISTENING_ADDRESS    = '0.0.0.0'/g" config.py \
    && python omnidb-server.py --init 

EXPOSE 8000

CMD python manage.py runasgi
