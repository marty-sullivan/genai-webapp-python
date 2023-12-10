FROM public.ecr.aws/docker/library/python:3.11-slim-bookworm as base

RUN pip install --no-cache poetry
RUN poetry config virtualenvs.create false

WORKDIR /code

COPY ./pyproject.toml ./poetry.lock* ./

RUN adduser --disabled-password --gecos '' streamlit

# Development Image
FROM base as development

RUN poetry install --no-interaction --no-ansi --no-root -vv

COPY ./app ./app

RUN poetry install --no-interaction --no-ansi -vv

USER streamlit
ENTRYPOINT ["streamlit"]
CMD [ "run", "app/Home.py", "--server.runOnSave", "true"]

# Production Image
FROM base as production

RUN poetry install --no-dev --no-interaction --no-ansi --no-root -vv

COPY ./app ./app
RUN poetry install --no-dev --no-interaction --no-ansi -vv

USER streamlit
ENTRYPOINT ["streamlit"]
CMD [ "run", "app/Home.py"]
