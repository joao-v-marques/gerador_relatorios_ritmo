# 🧠 RPA - Geração Automática de Relatórios Excel

Este projeto é um **RPA** desenvolvido em **Python**, criado para automatizar a geração de relatórios em formato **Excel (.xlsx)** a partir de dados armazenados em banco de dados.

## ⚙️ Funcionamento

1. O usuário executa o arquivo **.exe** da aplicação.  
2. O app envia uma requisição ao **controller**, solicitando os dados do relatório.  
3. O controller acessa o **banco de dados**, realiza a consulta e retorna os dados.  
4. A aplicação gera automaticamente uma **planilha Excel** utilizando a biblioteca `openpyxl`.  
5. É exibida uma janela para o usuário **escolher onde salvar o arquivo**.  

> 🔹 Todo o processo ocorre **sem interface gráfica**, garantindo rapidez e simplicidade.

## 🧩 Tecnologias Utilizadas

- **Python**
- **OpenPyXL** – geração e manipulação de arquivos Excel
- **Controle de Funções** – comunicação com o controller
- **Banco de Dados SQL** – origem dos dados do relatório

## 🚀 Objetivo do Projeto

Automatizar a geração e o download de relatórios empresariais, reduzindo o tempo gasto em tarefas manuais e eliminando erros humanos.  
O projeto demonstra o uso prático de **RPA em Python** aplicado a **processos corporativos reais** e uma arquitetura com controller simplificada.

## 🖥️ Como Executar

1. Baixe o executável `.exe` ou rode o script Python localmente.  
2. Ao iniciar, a aplicação fará todo o processo automaticamente.  
3. Quando o relatório estiver pronto, selecione o local de salvamento na janela exibida.  

## 📁 Estrutura Simplificada
├── controller/ # Controller responsável por consultar o banco
├── main.py # Código principal da automação
├── requirements.txt # Dependências do projeto
├── /dist # Arquivo .exe gerado pelo PyInstaller
└── README.md

## 🧑‍💻 Autor

**João Victor Marques**  
💼 Desenvolvedor Python | Automação | Flask | SQL  
📧 Contato: [joaovmarques2006@outlook.com] 
🌐 GitHub: [https://github.com/joao-v-marques]