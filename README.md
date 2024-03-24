# pdf に対する質問に解答してくれる RAG を作る

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

### chainlit のデフォルト port やホスト IP を変更したい(ブラウザからアクセスできなかった)

- [Chainlit で LLM アプリを試す](https://zenn.dev/kun432/scraps/d312ecea15726d)を見ると，`chainlit run`の設定変更は引数でできるが，`chailit hello'は環境変数でしか切り替えできない。
- また，`docker compose run`を使用してシェルから chailit を起動する際には compose.yml や Dockerfile の内容にかかわらず，port を開くオプションをつけないと port に対してコンテナ外からアクセス不可能なのて注意すること。

### chainlit で受け取ったメッセージがうまく解釈できない

- chainlit でユーザが送信したメッセージが chainlit.message.Message object なので.content を使って str に変換する必用がある。

---

## REFEREN

- [Lang Chain のチュートリアル](https://python.langchain.com/docs/expression_language/get_started)
- [pdf を使う RAG](https://qiita.com/hiroki_okuhata_int/items/7102bab7d96eb2574e7d)
