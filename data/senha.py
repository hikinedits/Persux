from data.ferramentas import *
from data.menu import senhaf


def senha():
    rnick = ''
    vn = os.path.exists('.Nick')
    if vn:
        rnick = open('.Nick', 'r')
    rcor = open('.Cor', 'r')
    print(senhaf)
    senhaa = str(input(f'{am}Senha: {br}'))
    senhab = str(input(f'{am}Confirme a senha: {br}'))
    if senhaa == senhab:
        ssenha = f'''
echo 'import os
from time import sleep
def menu():
    try:
        User = input("Senha: ")
        if User == "{senhab}":
         sleep(1)
         os.system("clear")
        elif User != "{senhab}":
         print("Senha Não identificada!")
         sleep(1)
         os.system("clear")
         menu()
    except:
         print("Senha Não identificada!")
         sleep(1)
         os.system("clear")
         menu()
menu()' >> usr.py
        python usr.py
rm -rf usr.py'''
        os.system('rm -rf .Senha')
        senha_file = open('.Senha', 'w')
        senha_file.write(ssenha)
        senha_file.close()
        rsenha = open('.Senha', 'r')
        bash = open('bash.bashrc', 'w')
        bash.write(f'{inicio}\n' + f'{rsenha.read()}\n{rnick.read()}\n{rcor.read()}' if vn
                   else f'{rsenha.read()}\n{rcor.read()}\n{final}')
        bash.close()
