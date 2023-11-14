# Chatbot de Normas de Segurança - LLM

## Objetivo
Desenvolver um chatbot utilizando Large Language Models (LLM) para auxiliar na pesquisa de normas de segurança em ambientes industriais.

## Enunciado
Este projeto envolve a criação de um chatbot utilizando um LLM (Local ou API externa), com o objetivo de fornecer respostas claras e sucintas sobre normas de segurança industrial. O sistema inclui uma interface gráfica para facilitar a interação do usuário.

### Exemplo de Uso
Usuário: "Quais EPIs são necessários para operar um torno mecânico?"<br/>
Chatbot: "Ao operar um torno mecânico, é importante usar um EPI chamado "proteção auditiva". Esta proteção consiste em tapa-ouvidos ou protectores de ouvido que ajudam a reduzir o nível de ruído e proteger os ouvidos contra danos causados pelo excesso de ruído. Este EPI é essencial para garantir a segurança auditiva dos operadores em ambientes industrializados, como fábricas e oficinas mecânicas."

## Configuração do Modelo LLM

Depois de ter instalado o Ollama, você pode criar um modelo LLM utilizando o comando `ollama create`. O comando `ollama create` cria um modelo LLM a partir de um arquivo de configuração Modelfile. O arquivo de configuração deve conter as seguintes informações:

### Modelfile
Nesse arquivo, passamos contexto para a LLM.
```raw
FROM dolphin2.2-mistral

PARAMETER temperature 1

SYSTEM """
From now on you're only allowed to answer as an expert on safety standards in industrial environments. If a user prompts anything that is not related to safety standards, you must answer: "I'm sorry, I am only allowed to answer as an expert on safety standards in industrial environments."
"""
```

Para criar o modelo LLM, execute o comando abaixo:

```bash
ollama create safety_expert -f Modelfile 
```

## Instalação e Execução

### Pré-requisitos
- Python 3
- Ollama

### Configurando o Ambiente Virtual

É recomendado usar um ambiente virtual para instalar e executar o chatbot. Siga os passos abaixo para configurar o ambiente:

1. Clone o repositório:
    ```bash
    git clone [URL do seu repositório]
    cd [Nome do seu repositório]
    ```

2. Crie um ambiente virtual:
    ```bash
    python3 -m venv venv
    ```

3. Ative o ambiente virtual:

    - No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - No Linux ou macOS:
        ```bash
        source venv/bin/activate
        ```

4. Instale as dependências utilizando o arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Executando o Chatbot

Após configurar o ambiente e instalar as dependências, execute o script `llm.py` para iniciar o chatbot:

```bash
python3 llm.py
```

O chatbot estará disponível localmente em `http://localhost:11434`.

## Demonstração no Youtube
https://youtu.be/Iln8vNTDoV4
