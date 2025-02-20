#Crie um sistema de chamados, o sistema deverá permitir:
#Cadastrar novos chamados
#Buscar chamados por ID ou descrição
#Remover chamados finalizados
#Listar chamados em ordem de prioridade
#Exibir estatísticas sobre os chamados
#Reverter e limpar a lista de chamados 
#Projeto deve ser inserido no Github, listado como público. 

chamados = []

# Função para cadastrar um novo chamado
def cadastrar_chamado(chamados, id, descricao, prioridade):
    chamado = {
        "id": id,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "aberto"
    }
    chamados.append(chamado)  # Adiciona o chamado à lista
    print(f"Chamado {id} cadastrado com sucesso!")

# Função para listar todos os chamados
def listar_chamados(chamados):
    if chamados:
        for chamado in chamados:
            print(f"ID: {chamado['id']}, Descrição: {chamado['descricao']}, Prioridade: {chamado['prioridade']}, Status: {chamado['status']}")
    else:
        print("Nenhum chamado registrado.")
# Função para finalizar chamados
def finalizar_chamados(chamados, id):
    for d in chamados:
        if d["id"] == id:
            d["status"] = 'finalizado'

# Função para remover chamados finalizados
def remover_chamados_finalizados(chamados):
    chamados[:] = [chamado for chamado in chamados if chamado["status"] != "finalizado"]
    print("Chamados finalizados removidos!")

# Função para listar chamados por prioridade
def listar_por_prioridade(chamados):
    chamados_ordenados = sorted(chamados, key=lambda x: x["prioridade"])
    listar_chamados(chamados_ordenados)

# Função para exibir estatísticas sobre os chamados
def exibir_estatisticas(chamados):
    total = len(chamados)
    finalizados = sum(1 for chamado in chamados if chamado["status"] == "finalizado")
    abertos = total - finalizados
    print(f"Total de chamados: {total}")
    print(f"Chamados abertos: {abertos}")
    print(f"Chamados finalizados: {finalizados}")

# Função para reverter e limpar a lista de chamados
def limpar_lista(chamados):
    chamados.clear()
    print("Lista de chamados limpa!")


def reverter_lista(chamados):
    chamados_invertido = chamados[::-1]
    print(chamados_invertido)

def buscar_chamados(chamados):
    criterio = input("Deseja buscar por ID ou Descrição? (Digite 'ID' ou 'Descrição'): ").lower()
    if criterio == 'id':
        id_busca = input("Digite o ID do chamado: ")
        encontrados = [chamado for chamado in chamados if chamado["id"] == id_busca]
    elif criterio == 'descrição':
        descricao_busca = input("Digite a descrição do chamado (ou parte dela): ").lower()
        encontrados = [chamado for chamado in chamados if descricao_busca in chamado["descricao"].lower()]
    else:
        print("Critério inválido! Use 'ID' ou 'Descrição'.")
        return
    
    if encontrados:
        for chamado in encontrados:
            print(f"ID: {chamado['id']}, Descrição: {chamado['descricao']}, Prioridade: {chamado['prioridade']}, Status: {chamado['status']}")
    else:
        print("Nenhum chamado encontrado.")


# Função para rodar o sistema de chamados
def rodar_sistema():
    while True:
        print("       *SISTEMAS DE CHAMADOS*        ")
        print("+===================================+")
        print("|1. Cadastrar Chamado               |")
        print("|2. Listar Chamados                 |")
        print("|3. Remover Chamados Finalizados    |")
        print("|4. Listar Chamados por Prioridade  |")
        print("|5. Exibir Estatísticas             |")
        print("|6. Limpar Lista de Chamados        |")
        print("|7. Inverter a Lista de Chamados    |")
        print("|8. Buscar Chamado                  |")
        print("|9. Finalizar Chamado               |")
        print("|10. Sair                           |")
        print("+===================================+")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Cadastrar um novo chamado
            id = f"{len(chamados) + 1}"
            descricao = input("Digite a descrição do chamado: ")
            prioridade = input("\nDigite a prioridade \n0 para prioridade maxima\n1 para prioridade alta\n2 para prioridade média\n3 para prioridade baixa\nDigite a prioridade: ")
            cadastrar_chamado(chamados, id, descricao, prioridade)
        elif opcao == "2":
            listar_chamados(chamados)
        elif opcao == "3": 
            remover_chamados_finalizados(chamados)
        elif opcao == "4":
            listar_por_prioridade(chamados)
        elif opcao == "5":
            exibir_estatisticas(chamados)
        elif opcao == "6":
            limpar_lista(chamados)
        elif opcao == "7":
            reverter_lista(chamados)
        elif opcao == "8":
            buscar_chamados(chamados)
        elif opcao == "9":
            id2 = input("Digite o ID do chamado para finalizar:")
            finalizar_chamados(chamados, id2)
        elif opcao == "10":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Iniciar o sistema
rodar_sistema()
