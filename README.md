# Agente Inteligente - Mercado Central 24h

Este repositório contém o código-fonte e a documentação do Agente Inteligente desenvolvido para o **Mercado Central 24h**, um supermercado moderno 24/7. O agente foi desenhado para atuar no atendimento ao cliente, consulta de FAQs, regras de negócios e políticas internas.

## 📝 Descrição Geral do Projeto
O projeto consiste em um Agente Inteligente construído para responder perguntas complexas em linguagem natural baseadas em uma base de conhecimento privada (arquivos PDF e dados tabulares). Ele visa desafogar o SAC, dando suporte imediato sobre horários, programas VIP, política de reembolso e compras logísticas, unificando a experiência da loja física com o e-commerce.

## 🏛️ Arquitetura da Solução
- **Interface/API:** Frontend em Streamlit (ou API FastAPI) para receber as consultas.
- **Orquestração GenAI:** LangChain para orquestrar o pipeline de RAG (Retrieval-Augmented Generation).
- **Processamento de Base de Conhecimento:** `PyPDF2` / `langchain-community` document loaders para extração de texto dos documentos operacionais do mercado.
- **Modelos:** 
  - Embeddings: HuggingFace / OpenAI embeddings para vetorização.
  - LLM: Modelo Generativo (como o Gemini ou OpenAI) para geração de respostas fluentes.
- **Infraestrutura Cloud:** Implantação efetuada no **Oracle Cloud Infrastructure (OCI)** utilizando OCI Compute Instances.

## 🛠️ Tecnologias e Ferramentas
- Python 3.10+
- LangChain & ChromaDB / FAISS (Vector Database)
- PyPDF2 / pdfplumber
- Streamlit
- Oracle Cloud Infrastructure (OCI)

## 🚀 Instruções para Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/agente-central24h.git
   cd agente-central24h
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure as chaves de API:
   Crie um arquivo `.env` na raiz do projeto contendo:
   ```env
   OPENAI_API_KEY=sua_chave_aqui
   # ou GOOGLE_API_KEY=sua_chave_aqui
   ```
5. Inicie a aplicação:
   ```bash
   streamlit run agente_inteligente.py
   ```

## 💬 Exemplos de Uso

**Pergunta do Cliente:** 
> "Comprei uma cerveja ontem à noite e hoje de manhã vi que a lata estava estufada. Como faço pra trocar?"

**Resposta Gerada pelo Agente:**
> "Olá! No Mercado Central 24h, prezamos pela qualidade dos nossos produtos. Por se tratar de um vício de qualidade em um produto não durável (bebida), você pode realizar a troca imediatamente. Basta se dirigir ao balcão do SAC presencial com a lata estufada e o seu Cupom Fiscal. Não é necessário abrir o produto para comprovar o problema, a própria embalagem estufada já é suficiente. Como a compra foi feita ontem, você está perfeitamente dentro do prazo de 30 dias para produtos não duráveis. Posso te ajudar com mais alguma dúvida?"

**Pergunta do Colaborador:**
> "Qual a temperatura ideal da câmara do hortifrúti?"

**Resposta Gerada pelo Agente:**
> "De acordo com as Normas de Segurança Alimentar e Vigilância Sanitária (ANVISA) da nossa loja, a temperatura ideal da câmara de vegetais (hortifrúti) é entre 8°C e 12°C. Essa verificação deve ser feita a cada 4 horas."
