FROM python:3.10-slim-bullseye

RUN apt-get update; \
    apt-get install -y --no-install-recommends wget nginx git python3-dev gcc; \
    rm -rf /var/lib/apt/lists/*; \
    wget -O - https://install.python-poetry.org | python -

ENV PATH /root/.local/bin:$PATH


COPY . /app
WORKDIR /app

RUN poetry config virtualenvs.create false \
    && poetry install

RUN chmod +x ./compose/local/docker-entrypoint.sh

ENTRYPOINT ["sh", "./compose/local/docker-entrypoint.sh" ]

