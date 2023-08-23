##Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
##A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).




def calcular_idade(ano_nascimento):
    ano_atual = 2022
    idade = ano_atual - ano_nascimento
    return idade

def main():
    try:
        print("Entre com seu ano de nascimento")
        ano_nascimento = int(input())       
        print("Entre com seu nome completo")
        nome_completo = input()

        if ano_nascimento < 1922 or ano_nascimento > 2021:
            raise ValueError()

        idade = calcular_idade(ano_nascimento)
        print("Nome:", nome_completo)
        print("Idade:", idade)
    except ValueError:
        print("Entre com um numero valido!")
  
main()
    
    

    

