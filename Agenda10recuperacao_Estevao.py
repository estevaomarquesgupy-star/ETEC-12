#Atividade Prática

def nome_da_funcao():
    # Esta função não faz nada, apenas serve como exemplo
    pass

def erro_acesso():
    print ("Acesso negado!")

    #funcoes sem parametro

    def sistema_iniciado():
        print("Sistema iniciado com sucesso!")

#funcoes com parametro

def erro_usuario(nome):
    print(f"Erro: Usuário {nome} não encontrado!")


    erro_usuario("Carlos")

#funcoes com retorno

def calcular_horas(entrada, saida):
    total = saida - entrada
    return total    

#uso do valor retornado

print(f"horas trabalhadas no dia: {calcular_horas(8, 17)}")

def nome_plano(cod_plano):
    if cod_plano == 1:
        return "Plano Básico"
    elif cod_plano == 2:
        return "Plano Intermediário"
    elif cod_plano == 3:
        return "Plano Avançado"
    else:
        return "Código de plano inválido"

    #

    def nome_plano(cod_plano):
        nome = "Plano invalido"

        if cod_plano == 1:
            nome = "Plano Básico"
        elif cod_plano == 2:
            nome = "Plano Intermediário"
        elif cod_plano == 3:
            nome = "Plano Avançado" 

            return nome

        #Atividade ETEC nota aluno

     




