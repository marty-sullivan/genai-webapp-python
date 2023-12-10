FROM public.ecr.aws/docker/library/python:3.11-slim-bookworm

RUN apt-get update \
    && apt-get install -y \
        curl \
        git \
        unzip \
        vim \
        wget \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean 

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-$(uname -m).zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install --update \
    && echo 'complete -C '/usr/local/bin/aws_completer' aws' >> ~/.bashrc \
    && rm -rf awscliv2.zip ./aws

RUN pip install --no-cache poetry
RUN poetry config virtualenvs.create false

WORKDIR /code

COPY ./pyproject.toml ./poetry.lock* ./

RUN poetry install --no-interaction --no-ansi -vv

WORKDIR /workspace

ENTRYPOINT ["tail", "-f", "/dev/null"]
