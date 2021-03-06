FROM ghcr.io/kurbezz/base_docker_images:3.10-postgres-asyncpg-poetry-buildtime as build-image

WORKDIR /root/poetry

COPY pyproject.toml poetry.lock /root/poetry/

RUN poetry export --without-hashes > requirements.txt \
    && . /opt/venv/bin/activate \
    && pip install -r requirements.txt --no-cache-dir


FROM ghcr.io/kurbezz/base_docker_images:3.10-postgres-runtime as runtime-image

WORKDIR /app

COPY ./src/ /app/
COPY ./scripts/ /root/

ENV VENV_PATH=/opt/venv
ENV PATH="$VENV_PATH/bin:$PATH"

COPY --from=build-image $VENV_PATH $VENV_PATH

EXPOSE 8080

CMD bash /root/start.sh
