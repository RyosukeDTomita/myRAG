# 

![un license](https://img.shields.io/github/license/RyosukeDTomita/LangChainTest)

## INDEX

- [ABOUT](#about)
- [LICENSE](#license)
- [ENVIRONMENT](#environment)
- [PREPARING](#preparing)
- [HOW TO USE](#how-to-use)
- [ERROR LOG](#error-log)
- [REFERENCE](#reference)

---

## ABOUT

---

## LICENSE

[un license](./LICENSE)

---

## ENVIRONMENT

- Python3.10: for detail, see [Dockerfile](./Dockerfile)
  - LCEL
  - Gradio

---

## PREPARING

- Buy OpenAi API [here](https://platform.openai.com/account/api-keys)

---

## HOW TO USE

1. edit [.env](./.env) to add your OpenAi API KEY

```shell
cat <<EOF >> .env
OPENAI_API_KEY="hogehoge"
EOF
```

<details><summary>Azure OpenAIを使う場合</summary><div>

```shell
cat <<EOF >> .env
OPENAI_API_VERSION=2023-12-01-preview
AZURE_OPENAI_ENDPOINT=https://example.com
AZURE_OPENAI_API_KEY=hogehoge
EOF
```

</div></details>

2. run Docker container

```shell
docker compose up
```

---

## ERROR LOG

---

## REFERENCE

- [Lang Chain のチュートリアル](https://python.langchain.com/docs/expression_language/get_started) をやってみるための環境構築をしました。
