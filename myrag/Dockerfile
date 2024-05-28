ARG PYTHON_VERSION=3.10.14
FROM python:${PYTHON_VERSION} as dependencies
ENV PIP_ARGS="--no-cache-dir"

WORKDIR /usr/local/app
COPY ./pyproject.toml ./poetry.lock* ./
RUN <<EOF
#apt-get update -y
#apt-get install pipx --no-install-recommends -y
#pipx ensurepath
#pipx install poetry==1.8.3
pip install --upgrade pip setuptools wheel --no-cache-dir
pip install poetry==1.8.3
poetry config virtualenvs.create false
poetry env use ${PYTHON_VERSION}
poetry install
rm -rf /var/lib/lists
EOF

#FROM dependencies AS app
COPY . .
EXPOSE 8000
