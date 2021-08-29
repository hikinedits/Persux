from data.ferramentas import *
from data.menu import coresf, menu_cores


def letra():
    while True:
        os.system('clear')
        vn = os.path.exists('.Nick')
        vs = os.path.exists('.Senha')
        print(coresf)
        print(menu_cores)
        cores = str(input(f'\n{am}//: {br}'))
        os.chdir('/data/data/com.termux/files/usr/etc')
        os.system('rm -rf bash.bashrc')
        if cores == '1':
            scor = cor_letra.replace(':cor', '31')
        elif cores == '2':
            scor = cor_letra.replace(':cor', '33')
        elif cores == '3':
            scor = cor_letra.replace(':cor', '37')
        elif cores == '4':
            scor = cor_letra.replace(':cor', '32')
        elif cores == '5':
            scor = cor_letra.replace(':cor', '36')
        elif cores == '6':
            scor = cor_letra.replace(':cor', '34')
        elif cores == '7':
            scor = cor_letra.replace(':cor', '35')
        else:
            print(f'{ve}{cores} não é um comando')
            sleep(2)
            os.system('clear')
            break
        os.system('rm -rf .Cor')
        cor_file = open('.Cor', 'w')
        cor_file.write(f'{scor}')
        cor_file.close()
        rcor = open('.Cor', 'r')
        bash = open('bash.bashrc', 'w')
        if vs:
            rsenha = open('.Senha', 'r')
        if vn:
            rnick = open('.Nick', 'r')
        if os.path.exists('.Cor'):
            bash.write((f'{inicio}\n') + (f'{rsenha.read()}\n{rnick.read()}'
                       if vs and vn else f'{rsenha.read()}' if not vn
                       else f'{rnick.read()}') + (f'\n{rcor.read()}{final}'))
        bash.close()
        break
