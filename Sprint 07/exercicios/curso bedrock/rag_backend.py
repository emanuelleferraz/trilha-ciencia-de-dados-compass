# Importações
import os
from langchain_community.document_loaders import PyPDFLoader  
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from langchain_aws import ChatBedrock  # Alterado de BedrockLLM para ChatBedrock

def hr_index():
    # Fonte dos dados e carregamento com PDFLoader
    data_load = PyPDFLoader('https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf')

    # Split do texto com RecursiveCharacterTextSplitter
    data_split = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=100,chunk_overlap=10)

    # Criando Embeddings com o Bedrock
    data_embeddings = BedrockEmbeddings(
        credentials_profile_name = '831926590523_ProgramaBolsaDataScience',
        model_id = 'amazon.titan-embed-text-v2:0')
    
    # Index Search
    data_index = VectorstoreIndexCreator(
        text_splitter = data_split,
        embedding = data_embeddings,
        vectorstore_cls = FAISS)
    
    # HR Policy
    db_index = data_index.from_loaders([data_load])
    return db_index

def hr_llm():
    llm = ChatBedrock(  # Alterado para ChatBedrock
        credentials_profile_name='831926590523_ProgramaBolsaDataScience',
        model_id='anthropic.claude-3-haiku-20240307-v1:0',
        model_kwargs={
            "max_tokens": 3000,
            "temperature": 0.1,
            "top_p": 0.9
        })
    return llm

# Buscando resposta do usuário
def hr_rag_response(index, question):
    rag_llm = hr_llm()
    hr_rag_query = index.query(question=question, llm=rag_llm)
    return hr_rag_query
