# Web Scraper B3 - Extração de Dados de Contratos em Aberto

Este projeto é um web scraper desenvolvido em Python utilizando a biblioteca Selenium. Ele coleta informações sobre contratos em aberto por tipo de participante no site da [B3 (Brasil, Bolsa, Balcão)](https://www.b3.com.br/) e armazena os dados em um arquivo CSV.

## Funcionalidades

- **Coleta de dados históricos**: O script busca dados a partir de uma data inicial configurável até 01/01/2004.
- **Armazenamento em CSV**: As informações são armazenadas em um arquivo CSV, separadas por `|`, com as seguintes colunas:
  - Data
  - Nome da Tabela
  - Tipo de Participante
  - Contratos de Compra
  - Percentual de Contratos de Compra
  - Contratos de Venda
  - Percentual de Contratos de Venda

## Requisitos

- [Python 3.x](https://www.python.org/downloads/)
- [Selenium](https://pypi.org/project/selenium/)
- [Webdriver para Google Chrome](https://sites.google.com/a/chromium.org/chromedriver/)

### Instalação do Selenium

Você pode instalar a biblioteca Selenium utilizando o pip:

```bash
pip install selenium
