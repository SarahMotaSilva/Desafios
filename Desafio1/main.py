from src.processamento import cadastrar_funcionario
from src.relatorio import gerar_texto_relatorio, salvar_em_arquivo


def main():
    banco_dados = []
    while True:
        print("\n1. Cadastrar | 2. Relatório | 3. Salvar | 4. Sair [cite: 14]")
        op = input("Opção: ")

        if op == "1":
            func = cadastrar_funcionario()
            if func:
                banco_dados.append(func)
        elif op == "2":
            if not banco_dados:
                print("Lista vazia.")
            else:
                print(gerar_texto_relatorio(banco_dados))
        elif op == "3":
            if not banco_dados:
                print("Nada para salvar.")
            else:
                salvar_em_arquivo(gerar_texto_relatorio(banco_dados))
        elif op == "4":
            print("Encerrando... [cite: 18]")
            break


if __name__ == "__main__":
    main()
