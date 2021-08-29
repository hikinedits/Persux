from data.menu import menu_nome
from data.ferramentas import *


def nome_letra():
    print(menu_nome)
    options = str(input(f'{am}//: {br}'))
    if options == '1':
        os.system('rm -rf .usuario')
        os.system('clear')
        user = str(input(f'{am}Nome: {ve}'))
        user_file = open('.usuario', 'w')
        user_file.write(user)
        user_file.close()
    else:
        print(f'{ve}Comando inválido!' if options != '2'
              else '')
        sleep(2 if options != '2'
              else 0.5)
        os.system('clear')
