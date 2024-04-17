import streamlit as st 
import openai 
from langchain.document_loaders import NotionDirectoryLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.embeddings import OpenAIEmbeddings 
from langchain.vectorstores import FAISS 

# OpenAI API キーをロード
openai.api_key = st.secrets[ "OPENAI_API_KEY" ] 

# 'test_notionContent'フォルダーにあるNotionコンテンツをロード
loader = NotionDirectoryLoader( "test_notionContent" ) 
documents =loader.load() 

# Notionコンテンツを小さなチャンクに分割
markdown_splitter = RecursiveCharacterTextSplitter( 
    separators=[ "#" , "## " , "###" , "\n\n" , "\n" , "." , "。"], 
    chunk_size= 1500 , 
    chunk_overlap= 100 ) 
docs = markdown_splitter.split_documents(documents) 

# OpenAI 埋め込みモデルの初期化
embeddings = OpenAIEmbeddings( ) 

# OpenAI 埋め込みモデルを使用してすべてのチャンクをベクトル埋め込みに変換
# すべてのベクトルをFAISSインデックスに保存し、ローカルフォルダー'faiss_index'に保存
db = FAISS.from_documents(docs, embeddings) 
db.save_local( "faiss_index" ) 

print ( 'Local FAISSインデックスは正常に保存されました。' )
