import os
import argparse
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def build_knowledge_base(pdf_path: str):
    print(f"Lendo documento: {pdf_path}...")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    print("Processando e dividindo textos...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = text_splitter.split_documents(documents)
    
    print("Criando banco vetorial (Embeddings)...")
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

def setup_agent(vectorstore):
    print("Inicializando Agente LLM...")
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
    )
    return qa_chain

if __name__ == "__main__":
    # Exemplo de execução via terminal
    parser = argparse.ArgumentParser(description="Agente Inteligente Mercado Central 24h")
    parser.add_argument("--doc", type=str, required=True, help="Caminho para o documento PDF/CSV fonte")
    args = parser.parse_args()
    
    # Valida se chave da API existe
    if not os.getenv("OPENAI_API_KEY"):
        print("ERRO: A variável de ambiente OPENAI_API_KEY não foi configurada.")
        exit(1)
        
    try:
        kb = build_knowledge_base(args.doc)
        agent = setup_agent(kb)
        
        print("\n=== Agente Iniciado! Digite 'sair' para encerrar. ===")
        while True:
            query = input("\nVocê: ")
            if query.lower() in ["sair", "exit", "quit"]:
                break
                
            response = agent.run(query)
            print(f"Agente Central 24h: {response}")
            
    except Exception as e:
        print(f"Ocorreu um erro na execução do Agente: {e}")
