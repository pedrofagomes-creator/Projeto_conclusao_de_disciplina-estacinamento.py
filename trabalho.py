# declaracões importantes
veiculos = []
CAPACIDADE_MAXIMA = 10

# funções ==================================================================================================
  
 # true se a placa bater
def validar_placa(placa):
    """Valida se a placa esta no formato AAA-1234."""
    placa = placa.upper().strip()
    if len(placa) != 8:
        return False
    if placa[3] != "-":
        return False
    letras = placa[:3]
    numeros = placa[4:]
    if not letras.isalpha():
        return False
    if not numeros.isdigit():
        return False
    return True

 # true se o horario bater
def validar_horario(horario):
    """Valida se o horario esta no formato HH:MM com valores validos."""
    if len(horario) != 5:
        return False
    if horario[2] != ":":
        return False
    horas = horario[:2]
    minutos = horario[3:]
    if not horas.isnumeric():
        return False
    if not minutos.isnumeric():
        return False
    hora_int = int(horas)
    minuto_int = int(minutos)
    if hora_int < 0 or hora_int > 23:
        return False
    if minuto_int < 0 or minuto_int > 59:
        return False
    return True

 # calcula o valor do estacionamento
def calcular_valor(minutos):
    """Calcula o valor a pagar com base no tempo de permanencia em minutos."""
    if minutos <= 60:
        return 5
    else:
        valor = 0
        extras = minutos - 60
        valor += 5
        blocos = extras // 15
        valor += blocos * 2
        resto = extras % 15
        if resto != 0:
            valor += 2
        return valor

 # junta tudo e adiciona na lista veiculos
def cadastrar_veiculo():
    """Registra a entrada de um novo veiculo no estacionamento."""
    if len(veiculos) >= CAPACIDADE_MAXIMA:
        print("Capacidade máxima atingida. Não foi possivel cadastrar.")
        return
    placa = input("Digite a placa: ").strip().upper()
    if not validar_placa(placa):
        print("Placa inválida. Use o formato ABC-1234")
        return
    for veiculo in veiculos:
        if veiculo["placa"] == placa:
            print("Essa placa ja esta cadastrada no estacionamento.")
            return
    horario = input("Digite o horário: ")
    if not validar_horario(horario):
        print("Horário inválido. Use o formato HH/MM (Exemplo: 08:30)")
        return
    tipo = input("Tipo do veiculo (carro / moto): ").strip().lower()
    if tipo != "carro" and tipo != "moto":
        tipo = "carro"
    for vaga in range(1, CAPACIDADE_MAXIMA + 1):
        ocupada = False
        for veiculo in veiculos:
            if veiculo["vaga"] == vaga:
                ocupada = True
        if not ocupada:
            veiculo_estacionado = {"placa" : placa, "entrada" : horario, "vaga" : vaga, "tipo" : tipo}
            veiculos.append(veiculo_estacionado)
            print(f"Veiculo {placa} cadastrado na vaga {vaga}")
            break
#saída de veículos
#converte horas para minutos
def horario_para_minutos(horario):
    horas = int(horario[:2])
    minutos = int(horario[3:])
    return horas * 60 + minutos
#remove os veículos
def remover_veiculo():
    """Registra a saida de um veiculo e calcula o valor a pagar."""
    placa = input("Placa do veiculo que esta saindo: ").strip().upper()
    veiculo_encontrado = None

    for veiculo in veiculos:
        if veiculo["placa"] == placa:
            veiculo_encontrado = veiculo
            break

    if veiculo_encontrado is None:
        print("Placa nao encontrada no estacionamento.")
        return

    horario_saida = input("Horario de saida (HH:MM): ")

    if not validar_horario(horario_saida):
        print("Horario invalido.Use o formato HH/M. (Por exemplo: 08:30)")
        return

    entrada_minutos = horario_para_minutos(veiculo_encontrado["entrada"])
    saida_minutos = horario_para_minutos(horario_saida)

    if saida_minutos < entrada_minutos:
        print("O horario de saida nao pode ser anterior ao de entrada.")
        return

    permanencia = saida_minutos - entrada_minutos

    valor = calcular_valor(permanencia)

    print("\n===== COMPROVANTE =====")
    print(f"Placa: {veiculo_encontrado['placa']}")
    print(f"Entrada: {veiculo_encontrado['entrada']}")
    print(f"Saida: {horario_saida}")
    print(f"Permanencia: {permanencia} min")
    print(f"Total a pagar: R$ {valor:.2f}")
    print(f"Vaga {veiculo_encontrado['vaga']} liberada.")

    veiculos.remove(veiculo_encontrado)

# consulta as vagas 
def consultar_vagas():
    """Exibe o numero de vagas disponiveis no estacionamento."""
    vagas = CAPACIDADE_MAXIMA - len(veiculos)
    print(f"Vagas disponiveis: {vagas}")

 # funções ==================================================================================================
#LISTA DE VEÍCULOS ESTACIONADOS 
def listar_veiculos() :
    """Exibe a tabela atualizada de veiculos."""
    if len (veiculos) == 0:
        print("NENHUM VEICULO ESTACIONADO")
        return
    
    print("\n===== VEICULOS ESTACIONADOS ====")
    print(f"{'Vaga' :<6} {'Placa' :<10} {"horário" :<6} {'   Tipo' :<8}")
    print("-" * 36)

    for veiculo in veiculos:
        print(f"{veiculo['vaga'] :<6} {veiculo['placa'] :<10} {veiculo['entrada'] :<10} {veiculo['tipo'] :<8}")
    print(f"\nTotal: {len(veiculos)} veiculo(s) estacionado(s)." )

 # loop base 
print("Bem vindo ao estacionamento")
def main():
    while True:
        print("==================================================")
        print("1 ENTRADA DE VEICULOS")
        print("2 SAIDA DE VEICULOS")
        print("3 LISTAR VEICULOS ESTACIONADOS")
        print("4 CONSULTAR VAGAS DISPONIVEIS")
        print("0 ENCERRAR")
        print("==================================================")

        opcao = input("Escolha uma opção: ")

        if not opcao.isdigit():
            print("Opcao invalida.")
            continue

        opcao = int(opcao)

    #chama as funções dependendo da opção 
        if opcao == 1:
            cadastrar_veiculo()
        elif opcao == 2:
            remover_veiculo()
        elif opcao == 3:
            listar_veiculos()
        elif opcao == 4:
            consultar_vagas()
        elif opcao == 0:
            print("Programa encerrado.")
            break
        else:
            print("Opcao invalida.")

if __name__=="__main__":
    main()


