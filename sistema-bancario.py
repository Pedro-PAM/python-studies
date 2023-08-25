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
    numSaque = 3
    numDepo = 0
    saldo = 0
    try:
        if opr == "s":
            saqueValid = True
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
            while(depositoValid == True):
                try:
                    if saldo<=0:
                        print("Saldo inválido!")
                    else:
                        depositoValid = False
                        oprValid = False
                        saldo += saldo
                        numDepo += 1
                        print("Depósito realizado com sucesso!")
                except:
                    print("Insira um número positivo...")       
                             
        elif opr == "e":          
            oprValid = False
            if saldo == 0:
                print("Não foram realizadas movimentações!")
            else:
                print(f'''Seu saldo é de R${saldo},
                      foram realizados {numDepo} depósitos,
                      e {numSaque} saques.''')
        else:
            print("Selecione uma operação válida!")
    except:
        print("Selecione uma operação disponível...")
    finally:
        print("Saindo...")