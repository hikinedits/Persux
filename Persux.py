from data.install import *
nms = 2
install()
from time import sleep
from data.menu import *


try:
    while True:
        os.system('clear')
        if nms == 1:
            print(f'{cy}~Lursy: {vd}Olá...')
            sleep(1)
            print('        É sua primeira vez por aqui?')
            sleep(3.5)
            os.system('clear')
            print(f'{cy}~Lursy: {vd}Bem... ')
            sleep(1)
            print('        Seja bem vindo!!')
            sleep(2)
            print('        Esse é o menu, fique a vontade :D')
            sleep(1.4)
        print(persuxf)
        print(menu_inicial)
        menu = int(input(f'{am}//: {br}'))
        if nms == 1 and menu < 4:
            print(f'{cy}~Lursy: {vd}Boa escolha!')
            sleep(1)
            nms = 3
        if menu == 1:
            from data.letra import letra
            letra()
        elif menu == 2:
            from data.banner import banner
            banner()
        elif menu == 3:
            from data.senha import senha
            senha()
        elif menu == 4:
            print(menu_nome)
            options = str(input(f'{am}//: {br}'))
            if options == '1':
                os.chdir('/data/data/com.termux/files/home/')
                os.system('rm -rf .usuario')
                os.system('clear')
                user = str(input(f'{am}Nome: {ve}'))
                user_file = open('.usuario', 'w')
                user_file.write(user)
                user_file.close()
                user = (open('.usuario', 'r')).readline()
                from data.menu import menu_inicial
                os.chdir('/data/data/com.termux/files/usr/etc/')
            else:
                print(f'{ve}Comando inválido!' if options != '2'
                      else '')
                sleep(2 if options != '2'
                      else 0.5)
                os.system('clear')
        elif menu == 5:
            print(f'\n{vd}Saindo...')
            sleep(1)
            os.system('clear')
            break
        else:
            print(f'{ve}Comando não reconhecido')
            sleep(1)
except KeyboardInterrupt:
    print(f'\n{vd}Saindo...')
    sleep(1)
    os.system('clear')
