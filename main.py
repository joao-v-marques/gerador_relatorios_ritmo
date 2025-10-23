from services.buscar_dados import buscar_dados
from services.gerar_excel import gerar_excel

if __name__ == '__main__':
    print("Rodando o script SQL...")
    dados = buscar_dados()

    if dados:
        print("Gerando excel...")
        gerar_excel(dados, "Estoque Novos")
    else:
        print("Nenhum dado encontrado")