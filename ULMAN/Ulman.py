import os
from Ulman_Disc import Daimonas


op = None
def main():
    global op
    while op != 0:
        os.system('clear')
        password = input('\nDigite a senha de mestre: ')
        os.system('clear')

        while password != 'fabuloso':
            os.system('clear')
            print('Você inseriu uma senha inválida, por favor tente novamente!')
            password = input('Digite a senha de mestre: ')

        print('Seja bem vindo a tela de mestre Ulman\n')
        print('-'*30)
        print('Escolha uma das opções a seguir:\n\n[ 0 ] - Sair.\n[ 1 ] - Bot Discord.\n[ 2 ] - Bot Instagram.\n')
        op = int(input('Digite o número referente a opção escolhida: '))

        while op < 0 and op > 2:
            print('Opção inválida. Tente novamente!')
            op = int(input('Digite o número referente a opção escolhida: '))

        if op == 0:
            os.close

        elif op == 1:
            Daimonas.daimonas()
            
        elif op == 2:
            print('Ainda estamos em desenvolvimento!')

        print('ENCERRADO!')

main()