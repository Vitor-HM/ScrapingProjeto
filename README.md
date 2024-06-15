## Sobre o Projeto
Esse projeto foi feito para colocar em pratica alguns aprendizados:

* **Estrutura de um projeto de dados**

* **Familiarizar-se com ferramentas de desenvolvimento**

* **Webscraping**



## Pré-requisitos

* **VSCode**: Editor de Código utilizado

* **Git e GitHub**:
1. Você deve ter o Git instalado em sua máquina.
2. Você também deve ter uma conta no GitHub.

### Instalação e Configuração

1. Clone o repositorio
```bash
git clone https://github.com/Vitor-HM/ScrapingProjeto
cd ScrapingProjeto
```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
```bash
python -m venv .venv
source .venv/Scripts/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. Execute o comando de execucão da pipeline para realizar a ETL:
```bash
task run
```

5. Execute o comando para ver a documentacao de forma local:
```bash
task docs
```

6. Execute os seguintes comandos para acessar o site local
```bash
cd streamlit
streamlit run app.py
```