FROM python:3.11.6-alpine3.18

# Set environment varibles
RUN apk update --no-cache &&  \
    apk add --no-cache unit-python3 curl libpq-dev gcc libc-dev libffi-dev g++ tzdata &&  \
    apk upgrade --no-cache

ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    TZ=Europe/Istanbul \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1


WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt && \
    pip install --upgrade wheel && \
    pip install --upgrade setuptools && \
    pip install --upgrade requests


WORKDIR /code
COPY ./app /code/app
COPY ./docker/config/nginx/*.json /docker-entrypoint.d/
COPY ./docker/config/entrypoint.sh /opt/entrypoint.sh

RUN chown -R unit:unit /code/app && \
    chmod 777 /opt/*.sh && \
    ln -sf /dev/stdout /var/log/unit.log

ENTRYPOINT ["/opt/entrypoint.sh"]
STOPSIGNAL SIGTERM

CMD ["unitd", "--no-daemon", "--control", "unix:/var/run/control.unit.sock"]