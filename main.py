from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep 
from datetime import datetime, timedelta
import csv

# Cabeçalho do arquivo CSV ------------------------------------------------------------------
nome_arquivo = "dados_temp.csv"

cabecalho = [
    "Data",
    "Nome_Tabela",
    "Tipo_Participante",
    "Contratos_Compra",
    "Contratos_Compra_Percentual",
    "Contratos_Venda",
    "Contratos_Venda_Percentual"
]

# Criar o arquivo CSV com o cabeçalho
with open(nome_arquivo, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(cabecalho)  # Escrever o cabeçalho
# --------------------------------------------------------------------------------------------

# Função para adicionar novas linhas ---------------------------------------------------------
def adicionar_linha(dados_linha):
    with open(nome_arquivo, mode='a', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(dados_linha)  # Escrever os dados da linha
# --------------------------------------------------------------------------------------------

try:
    # Inicia driver
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Vai até a URL
    driver.get('https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-de-derivativos/contratos-em-aberto/por-tipo-de-participante/')
    sleep(1)

    # Muda para o iframe
    iframe = driver.find_element(By.ID, 'bvmf_iframe')
    driver.switch_to.frame(iframe)
    sleep(1)

    # Definir a data inicial e final
    data_inicial = '01/01/2004'
    data = datetime.strptime(data_inicial, '%d/%m/%Y')

    print('\n')
    while True: # Loop infinito para todas as datas -----------------------------------------------
        data_str = data.strftime('%d/%m/%Y')
        if data_str == '31/12/2003':
            print()
            print('-'*50)
            print(' ||| Extração realizada até 01/01/2004! ')
            print()
            break

        print('>>>', data_str)

        # Buscando pela data em específico
        campo_data = driver.find_element(By.ID, 'dData1')
        campo_data.send_keys(data_str)
        sleep(0.5)
        campo_data.send_keys(Keys.ENTER)
        sleep(0.5)

        btn_data = driver.find_element(By.XPATH, '//*[@id="divContainerIframeBmf"]/div[1]/div/form/div/div[2]/button')
        btn_data.click()
        sleep(1)
        elemento = driver.find_element(By.ID, 'divContainerIframeBmf')
        sleep(0.5)

        tabelas = elemento.find_elements(By.TAG_NAME, 'table')
        for tabela in tabelas:

            nome_tabela = tabela.find_element(By.TAG_NAME, 'caption').text
            corpo = tabela.find_element(By.TAG_NAME, 'tbody')
            linhas = corpo.find_elements(By.TAG_NAME, 'tr')
            
            for linha in linhas:
                # Cria uma lista para as informações
                info = []
                info.append(data_str) # Adiciona o dia 
                info.append(nome_tabela) # Adiciona o nome da tabela

                # Primeiro, dividimos a linha por espaços
                texto_linha = linha.text
                elementos_linha = texto_linha.split()

                # Em seguida, separamos os valores numéricos do restante
                nome = ' '.join(elementos_linha[:-4])  # Os primeiros elementos são o nome
                valores = elementos_linha[-4:]  # Os últimos quatro elementos são os valores
                info.append(nome) # Adiciona o nome
                for valor in valores:
                    info.append(valor) # Adiciona cada valor (nas suas respectivas posições)

                adicionar_linha(info)
        
        # Quando terminar de rodar as tabelas do dia atual, subtrai um dia
        data -= timedelta(days=1)
        sleep(2)

except Exception as e:
    print('-' * 50)
    print('Erro:')
    print(e)
    input()
    print('\n')
