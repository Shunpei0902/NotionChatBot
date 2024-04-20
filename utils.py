import streamlit as st
import openai
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate

openai.api_key = st.secrets["OPENAI_API_KEY"]

@st.cache_resource
def load_chain():
  """
    The `load_chain()` function initializes and configures a conversational retrieval chain for
    answering user questions.
    :return: The `load_chain()` function returns a ConversationalRetrievalChain object.
    """

  # Load OpenAI embedding model
  embeddings = OpenAIEmbeddings()
  
  # Load OpenAI chat model
  llm = ChatOpenAI(temperature=0)
  
  # Load our local FAISS index as a retriever
  vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
  retriever = vector_store.as_retriever(search_kwargs={"k": 3})
  
  # Create memory 'chat_history' 
  memory = ConversationBufferWindowMemory(k=3,memory_key="chat_history")
  
  # Create system prompt
  template = """
  あなたはエンジニアの個人ナレッジメモについての質問に答えるAIアシスタントです。
  長い文書から抽出された以下の部分と質問が与えられます。会話形式で答えを提供してください。
  もし答えがわからなければ、「申し訳ありませんが、わかりません…😔」と言ってください。
  答えをでっち上げないでください。
  もし質問がエンジニアの個人ナレッジメモに関するものでなければ、あなたがエンジニアの個人ナレッジメモに関する質問のみに答えるよう設定されていることを丁寧に伝えてください。
  
  {context}
  質問: {question}
  役に立つ答え:"""
  
  # Create the Conversational Chain
  chain = ConversationalRetrievalChain.from_llm(llm=llm, 
                                              retriever=retriever, 
                                              memory=memory, 
                                              get_chat_history=lambda h : h,
                                              verbose=True)
  
  # Add systemp prompt to chain
  # Can only add it at the end for ConversationalRetrievalChain
  QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"],template=template)
  chain.combine_docs_chain.llm_chain.prompt.messages[0] = SystemMessagePromptTemplate(prompt=QA_CHAIN_PROMPT)
  
  return chain