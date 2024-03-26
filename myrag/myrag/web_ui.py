import chainlit as cl
from rag_engine import chat


@cl.on_chat_start
async def on_chat_start():
    """_summary_
    ページ訪問時の送信メッセージ。
    """
    await cl.Message(content="こんにちは！\n"
                     "私はhttps://www.justice.gov/criminal-oia/page/file/1153436/downloadに対する質問をに解答できます。").send()


@cl.on_message
async def on_message(input_message):

    # NOTE: input_messageはchainlit.message.Message objectなので.contentでstrを取得できる。
    result = chat(input_message.content)
    await cl.Message(content=result).send()
