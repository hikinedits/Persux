from data.ferramentas import *
from data.menu import bannerf, menu_cores


def banner():
    erro = 0
    rsenha = ''
    os.system('clear')
    print(bannerf)
    nick = str(input(f'{am}Nick: {br}'))
    banner_nick = banner_nick.replace(':name', f'{nick}')
    rnick = open('.Nick', 'r')
    rcor = open('.Cor', 'r')
    vs = os.path.exists('.Senha')
    if vs:
        rsenha = open('.Senha', 'r')
    print(menu_cores)
    name = str(input(f'\n{am}//: {br}'))
    os.chdir('/data/data/com.termux/files/usr/etc')
    os.system('rm -rf bash.bashrc')
    if name == '1':
        snick = banner_nick.replace(':cor', '31')
    elif name == '2':
        snick = banner_nick.replace(':cor', '33')
    elif name == '3':
        snick = banner_nick.replace(':cor', '37')
    elif name == '4':
        snick = banner_nick.replace(':cor', '32')
    elif name == '5':
        snick = banner_nick.replace(':cor', '36')
    elif name == '6':
        snick = banner_nick.replace(':cor', '34')
    elif name == '7':
        snick = banner_nick.replace(':cor', '35')
    else:
        print(f'{ve}{cores} não é um comando')
        sleep(2)
        os.system('clear')
        erro = 1
    if erro == 0:
        nick_file = open('.Nick', 'w')
        nick_file.write(f'{snick}')
        nick_file.close()
        rnick = open('.Nick', 'r')
        bash = open('bash.bashrc', 'w')
        bash.write(f'{inicio}\n' + f'{rsenha.read()}\n{rnick.read()}\n{rcor.read()}'if vs
                   else f'{rnick.read()}\n{rcor.read()}\n{final}')
        bash.close()
        rnick.close()
        os.system('clear')
