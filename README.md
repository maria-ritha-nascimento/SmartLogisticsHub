# **Smart Logistics Hub**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)  
**Repositório GitHub:** [Smart Logistics Hub](https://github.com/maria-ritha-nascimento/SmartLogisticsHub.git)

## **Descrição do Projeto**
O **Smart Logistics Hub** é uma solução inteligente para gerenciamento logístico, projetada para otimizar o rastreamento e gerenciamento de pacotes. A aplicação fornece uma API RESTful para realizar operações como cadastro, consulta, atualização e exclusão de pacotes. Com funcionalidades de filtro e documentação integrada via Swagger, o sistema é flexível, robusto e fácil de usar.

---

## **Descrição Técnica**
A arquitetura do projeto utiliza **Flask**, um framework minimalista em Python, junto com **Flask-RESTx** para construção da API e documentação automática. O banco de dados é gerenciado com **SQLAlchemy**, com suporte ao SQLite por padrão. O sistema é modular e pode ser facilmente adaptado para diferentes necessidades logísticas.

### **Principais Tecnologias**
- **Linguagem:** Python 3.9+
- **Framework:** Flask
- **Banco de Dados:** SQLite (padrão)
- **Documentação da API:** Swagger (via Flask-RESTx)

---

## **Funcionalidades**
- **CRUD Completo:** Criação, leitura, atualização e exclusão de pacotes.
- **Filtros:** Consulta de pacotes por status e destino.
- **Documentação Automática:** Interface Swagger para testar as rotas.
- **Banco de Dados Relacional:** Persistência eficiente dos dados com SQLAlchemy.

---

## **Como Executar o Projeto**
Siga as etapas abaixo para configurar e executar o projeto localmente:

### **Pré-requisitos**
1. **Python 3.9+ instalado:**  
   Verifique se o Python está instalado executando:
   ```bash
   python --version
   ```

2. **Git instalado:**  
   Garanta que você tenha o Git instalado para clonar o repositório:
   ```bash
   git --version
   ```

---

### **Passo a Passo**

#### **1. Clonar o repositório**
Clone o projeto para sua máquina local:
```bash
git clone https://github.com/maria-ritha-nascimento/SmartLogisticsHub.git
```

Entre no diretório do projeto:
```bash
cd SmartLogisticsHub
```

#### **2. Criar e ativar o ambiente virtual**
Crie um ambiente virtual para isolar as dependências:
```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/MacOS:**
  ```bash
  source venv/bin/activate
  ```

#### **3. Instalar dependências**
Instale todas as dependências do projeto:
```bash
pip install -r requirements.txt
```

#### **4. Configurar o banco de dados**
Execute o comando abaixo para criar o banco de dados:
```bash
python main.py
```

---

### **Como Acessar**
1. Inicie o servidor:
   ```bash
   python main.py
   ```
2. Acesse a aplicação no navegador em:
   ```
   http://127.0.0.1:5000/
   ```
3. A interface Swagger estará disponível para explorar e testar as APIs.

---

## **Exemplo de Uso**
### **1. Criar um pacote**
- **Endpoint:** `POST /packages`
- **Corpo da requisição:**
  ```json
  {
    "origin": "São Paulo",
    "destination": "Rio de Janeiro",
    "status": "pending"
  }
  ```

### **2. Listar pacotes com filtros**
- **Endpoint:** `GET /packages`
- **Parâmetros opcionais:**
  - `status`: Filtrar por status (e.g., "pending").
  - `destination`: Filtrar por destino (e.g., "Rio de Janeiro").

---

## **Contribuição**
Contribuições são bem-vindas! Siga os passos abaixo para contribuir:
1. Crie um fork do repositório.
2. Crie uma branch para suas alterações:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça o commit das alterações:
   ```bash
   git commit -m "Adiciona minha nova feature"
   ```
4. Envie para o GitHub:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request no repositório principal.

---

## **Licença**
Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

