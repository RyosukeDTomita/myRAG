FROM python:3.10.14 as depencencies

WORKDIR /usr/local/app
COPY ./pyproject.toml ./poetry.lock* ./
RUN <<EOF
pip install --upgrade pip setuptools wheel --no-cache-dir
pip install poetry==1.8.2 --no-cache-dir && poetry config virtualenvs.create false
pip install jupyter
poetry install
EOF

FROM depencencies AS app
COPY . .
EXPOSE 8000
