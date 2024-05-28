"""
pdfファイルを読み込んで、質問に答えるRAG
"""
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.globals import set_debug, set_verbose
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

set_debug(True)
set_verbose(True)


def create_index_tools() -> Chroma:
    """_summary_
    vector storeを作って返す。

    Returns:
        Chroma: vector store(index)
    """
    raw_documents = PyPDFLoader("./input_index/cloud_act.pdf").load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(raw_documents)
    vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
    return vectorstore


def chat(message: str) -> str:
    """
    vectore storeの内容を基に`message`に解答する。
    """
    template = """Answer the question based only on the following context:
    {context}

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    model = ChatOpenAI()
    vectorstore = create_index_tools()
    retriever = vectorstore.as_retriever()
    output_parser = StrOutputParser()
    setup_and_retrieval = RunnableParallel(
        {"context": retriever, "question": RunnablePassthrough()}
    )
    chain = setup_and_retrieval | prompt | model | output_parser
    result = chain.invoke(message)
    print(result)
    return result


def main():
    # テスト用
    chat("What is US Cloud Act? Answer within 50 words in Japanese.")


if __name__ == "__main__":
    main()
