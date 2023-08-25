## Criar um sistema bancário com as operações: sacar, depositar e extrato.

## Menu
print('''
      =============== MENU ==================
                    Bem vindo!
    Selecione sua operação:
    
    [d] = Depósito
    [s] = Saque
    [e] = Extrato
    
    ''')
opr = input()
oprValid = True
while(oprValid == True):
    try:
        if opr == "s":
            saqueValid = True
            numSaque = 3
            print("Escolha um valor para saque...")
            saque = int(input())
            while(saqueValid == True):
                try:
                    if saque>500 and saque<saldo and numSaque<=0:
                        print("Saque inválido!")
                    else:
                        oprValid = False
                        numSaque -= numSaque
                        saqueValid = False
                        saldo = saldo - saque
                        print("Saque realizado com sucesso!")    
                        print("Há apenas " + numSaque + " restantes...")        
                except:
                    print("Insira um valor válido...")               
            
        elif opr == "d":
            print("Digite o valor de seu depósito.")
            saldo = int(input())
            depositoValid = True
            numDepo = 0
            while(depositoValid == True):
                try:
                    if saldo<=0:
                        print("Saldo inválido!")
                    else:
                        depositoValid == False
                        oprValid == False
                        saldo += saldo
                        numDepo += 1
                        print("Depósito realizado com sucesso!")
                except:
                    print("Insira um número positivo...")       
                             
        elif opr == "e":
            if (numSaque == 3 and numDepo == 0):
                print("Não foram realizadas movimentações")
            else:
                print('''Seu saldo atual é R${saldo}.
                            Foram realizados {numDepo} depósitos,
                            e {numSaque} Saques.'''
                      )
            
        else:
            print("Selecione uma operação válida!")
    except:
        print("Selecione uma operação disponível...")

