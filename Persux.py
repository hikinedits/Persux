from time import sleep
import os

# Cores
ve = '\033[1;31m'  # Vermelho
vd = '\033[1;32m'  # Verde
am = '\033[1;33m'  # Amarelo
az = '\033[1;34m'  # Azul
br = '\033[1;37m'  # Branco
cy = '\033[1;36m'  # Ciano
rx = '\033[0;35m'  # Roxo


inicio = '''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth
'''

banner = '''echo -e '\e[0;~COR~m'
figlet ~N~
echo -e '\e[m\n' '''
ac = f'figlet ~N~ |lolcat -a -d 25'
Branco = '''PROMPT_DIRTRIM=2
PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[1;~COR~m\] '

if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
'''
nms = 2

# Instalção
Ver = os.path.exists('.Instalação')
if not Ver:
    os.system('clear')
    os.system('pkg install figlet -y')
    os.system('pkg install ruby -y')
    os.system('y')
    os.system('clear')
    os.chdir('/data/data/com.termux/files/home/')
    os.system('git clone https://github.com/busyloop/lolcat')
    os.system('clear')
    os.chdir('/data/data/com.termux/files/home/lolcat/bin/')
    os.system('gem install lolcat')
    os.system('clear')
    os.chdir('/data/data/com.termux/files/home/')
    os.system('rm -rf lolcat')
    os.chdir('/data/data/com.termux/files/usr/etc/')
    os.system('rm -rf motd')
    os.chdir('/data/data/com.termux/files/home/')
    Ins = open('.Instalação', 'a')
    Ins.write('By_Matheus')
    os.system('clear')
    nms = 1

os.chdir('/data/data/com.termux/files/usr/etc/')
vn = os.path.exists('.Nick')
vs = os.path.exists('.Senha')
vc = os.path.exists('.Cor')
cont = 1

senha = ''
pss = ''
nick = ''
cor = ''

try:
    s = 0
    while s != 4:

            os.system('clear')
            print(rx)
            if nms != 1:
                os.system('figlet Persux')
                print(f'''{br}
[1] - Mudar cor da letra
[2] - Mudar banner
[3] - Mudar senha
[4] - Sair''')
            else:
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
                print(rx)
                os.system('figlet Persux')
                print(f'''{br}
[1] - Adicionar cor da letra
[2] - Adicionar banner
[3] - Adicionar senha
[4] - Sair''')
            try:
                menu = int(input(f'{am}//: {br}'))
                if nms == 1 and menu < 4:
                    print(f'{cy}~Lursy: {vd}Boa escolha!')
                    sleep(1)
                    nms = 3
                if menu == 1:
                    os.system('clear')
                    if vs:
                        senha = open('.Senha', 'r')
                    if vn:
                        nick = open('.Nick', 'r')
                    print(az)
                    os.system('figlet Cores')
                    print(f'''
{am}[1] {br}- Verde
{am}[2] {br}- Azul
{am}[3] {br}- Branco
{am}[4] {br}- Amarelo
{am}[5] {br}- Vermelho
{am}[6] {br}- Voltar''')
                    cores = int(input(f'\n{am}//: {br}'))
                    if cores == 1:
                        os.system('rm -rf .Cor')
                        pc = open('.Cor', 'w')
                        pc.write(f'{Branco.replace("32", "34").replace("~COR~", "32")}')
                        pc.close()
                        cor = open('.Cor', 'r')
                        os.system('rm -rf bash.bashrc')
                        bash = open('bash.bashrc', 'w')
                        if vn and vs:
                            bash.write(f'{inicio}\n{senha.read()}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                        elif not vn and not vs:
                            bash.write(f'{inicio}\n{cor.read()}')
                            bash.close()
                        else:
                            if vn:
                                bash.write(f'{inicio}\n{nick.read()}\n{cor.read()}')
                                bash.close()
                            else:
                                bash.write(f'{inicio}\n{senha.read()}\n{cor.read()}')
                                bash.close()
                    elif cores == 2:
                        os.system('rm -rf .Cor')
                        pc = open('.Cor', 'w')
                        pc.write(f'{Branco.replace("~COR~", "34")}')
                        pc.close()
                        cor = open('.Cor', 'r')
                        os.system('rm -rf bash.bashrc')
                        bash = open('bash.bashrc', 'w')
                        if vn and vs:
                            bash.write(f'{inicio}\n{senha.read()}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                        elif not vn and not vs:
                            bash.write(f'{inicio}\n{cor.read()}')
                            bash.close()
                        else:
                            if vn:
                                bash.write(f'{inicio}\n{nick.read()}\n{cor.read()}')
                                bash.close()
                            else:
                                bash.write(f'{inicio}\n{senha.read()}\n{cor.read()}')
                                bash.close()
                    elif cores == 3:
                        os.system('rm -rf .Cor')
                        pc = open('.Cor', 'w')
                        pc.write(f'{Branco.replace("~COR~", "37")}')
                        pc.close()
                        cor = open('.Cor', 'r')
                        os.system('rm -rf bash.bashrc')
                        bash = open('bash.bashrc', 'w')
                        if vn and vs:
                            bash.write(f'{inicio}\n{senha.read()}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                        elif not vn and not vs:
                            bash.write(f'{inicio}\n{cor.read()}')
                            bash.close()
                        else:
                            if vn:
                                bash.write(f'{inicio}\n{nick.read()}\n{cor.read()}')
                                bash.close()
                            else:
                                bash.write(f'{inicio}\n{senha.read()}\n{cor.read()}')
                                bash.close()
                    elif cores == 4:
                        os.system('rm -rf .Cor')
                        pc = open('.Cor', 'w')
                        pc.write(f'{Branco.replace("~COR~", "33")}')
                        pc.close()
                        cor = open('.Cor', 'r')
                        os.system('rm -rf bash.bashrc')
                        bash = open('bash.bashrc', 'w')
                        if vn and vs:
                            bash.write(f'{inicio}\n{senha.read()}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                        elif not vn and not vs:
                            bash.write(f'{inicio}\n{cor.read()}')
                            bash.close()
                        else:
                            if vn:
                                bash.write(f'{inicio}\n{nick.read()}\n{cor.read()}')
                                bash.close()
                            else:
                                bash.write(f'{inicio}\n{senha.read()}\n{cor.read()}')
                                bash.close()
                    elif cores == 5:
                        os.system('rm -rf .Cor')
                        pc = open('.Cor', 'w')
                        pc.write(f'{Branco.replace("~COR~", "31")}')
                        pc.close()
                        cor = open('.Cor', 'r')
                        os.system('rm -rf bash.bashrc')
                        bash = open('bash.bashrc', 'w')
                        if vn and vs:
                            bash.write(f'{inicio}\n{senha.read()}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                        elif not vn and not vs:
                            bash.write(f'{inicio}\n{cor.read()}')
                            bash.close()
                        else:
                            if vn:
                                bash.write(f'{inicio}\n{nick.read()}\n{cor.read()}')
                                bash.close()
                            else:
                                bash.write(f'{inicio}\n{senha.read()}\n{cor.read()}')
                                bash.close()
                    elif cores == 6:
                        os.system('clear')
                    else:
                        print(f'{ve}Comando não identificado...')
                        sleep(1)

                elif menu == 2:
                    rmn = 0
                    if vc:
                        cor = open('.Cor', 'r')
                    if vs:
                        senha = open('.Senha', 'r')
                    def rn():
                        vn = os.path.exists('.Nick')
                        if vn:
                            os.system('clear')
                            print(rx)
                            os.system("figlet Banner")
                            print(f'''
{am}[1] {br}- Modificar banner
{am}[2] {br}- Remover banner''')
                            rem = int(input(f'{am}//: {br}'))
                            if rem == 2:
                                os.system('rm -rf .Nick')
                                os.system('rm -rf bash.bashrc')
                                bash = open('bash.bashrc', 'w')
                                cor = open('.Cor', 'r')
                                senha = open('.Senha', 'r')
                                vs = os.path.exists('.Senha')
                                if vs:
                                    bash.write(f'{inicio}\n{senha}\n{cor.read()}')
                                    bash.close()
                                else:
                                    bash.write(f'{inicio}\n{cor.read()}')
                                    bash.close()
                                global rmn
                                rmn = 1
                            elif rem == 1:
                                sleep(1)
                            else:
                                print(f'{ve}Comando inválido...')
                                sleep(1)
                                os.system('clear')
                                rn()
                    rn()
                    os.system('clear')
                    if rmn == 1:
                        print(f'{ve}Para sair use CRTL+c')
                    print(ve)
                    os.system('figlet banner')
                    name = input(f'{am}Nick:{br} ')
                    sleep(1)
                    print(f'''\n\n{am}CORES
{am}[1] {br}- Vermelho
{am}[2] {br}- Amarelo
{am}[3] {br}- Verde
{am}[4] {br}- Azul
{am}[5] {br}- Colorido
{am}[6] {br}- Voltar''')
                    cores = int(input(f'\n{am}//: {br}'))
                    os.system('rm -rf .Nick')
                    if cores == 1:
                        nb = open('.Nick', 'a')
                        nb.write(banner.replace('~N~', name).replace('~COR~', '31'))
                        nb.close()
                        nick = open('.Nick', 'r')
                        bash = open('bash.bashrc', 'w')
                        if vs:
                            bash.write(f'{inicio}\n{senha.read()}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                        else:
                            bash.write(f'{inicio}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                    elif cores == 2:
                        nb = open('.Nick', 'a')
                        nb.write(banner.replace('~N~', name).replace('~COR~', '33'))
                        nb.close()
                        nick = open('.Nick', 'r')
                        bash = open('bash.bashrc', 'w')
                        if vs:
                            bash.write(f'{inicio}\n{senha.read()}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                        else:
                            bash.write(f'{inicio}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                    elif cores == 3:
                        nb = open('.Nick', 'a')
                        nb.write(banner.replace('~N~', name).replace('~COR~', '32'))
                        nb.close()
                        nick = open('.Nick', 'r')
                        bash = open('bash.bashrc', 'w')
                        if vs:
                            bash.write(f'{inicio}\n{senha.read()}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                        else:
                            bash.write(f'{inicio}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                    elif cores == 4:
                        nb = open('.Nick', 'a')
                        nb.write(banner.replace('~N~', name).replace('~COR~', '34'))
                        nb.close()
                        nick = open('.Nick', 'r')
                        bash = open('bash.bashrc', 'w')
                        if vs:
                            bash.write(f'{inicio}\n{senha.read()}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                        else:
                            bash.write(f'{inicio}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                    elif cores == 5:
                        nb = open('.Nick', 'a')
                        nb.write(ac.replace('~N~', name))
                        nb.close()
                        nick = open('.Nick', 'r')
                        bash = open('bash.bashrc', 'w')
                        if vs:
                            bash.write(f'{inicio}\n{senha.read()}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                        else:
                            bash.write(f'{inicio}\n{nick.read()}\n{cor.read()}')
                            bash.close()
                    elif cores == 6:
                        os.system('clear')
                    else:
                        print(f'{ve}Comando não identificado...')
                        sleep(1)
                        os.system('clear')

                elif menu == 3:
                    rms = 0
                    if vn:
                        nick = open('.Nick', 'r')
                    if vc:
                        cor = open('.Cor', 'r')
                    def rs():
                        vs = os.path.exists('.Senha')
                        if vs:
                            os.system('clear')
                            print(rx)
                            os.system("figlet Senha")
                            print(f'''\n\n
{am}[1] {br}- Modificar senha
{am}[2] {br}- Remover senha''')
                            rem = int(input(f'{am}//: {br}'))
                            if rem == 1:
                                sleep(1)
                            elif rem == 2:
                                os.system('rm -rf .Senha')
                                cor = open('.Cor', 'r')
                                nick = open('.Nick', 'r')
                                bash = open('bash.bashrc', 'w')
                                vn = os.path.exists('.Nick')
                                if vn:
                                    bash.write(f'{inicio}\n{nick.read()}\n{cor.read()}')
                                else:
                                    bash.write(f'{inicio}\n{cor.read()}')
                                global rms
                                rms = 1
                            else:
                                print(f'{ve}Comando inválido!')
                                rs()
                    rs()
                    os.system('clear')
                    if rms == 1:
                        print(f'{ve}Para sair use CRTL+c')
                    print(vd)
                    os.system('figlet Senha')
                    senhab = input(f'{am}Senha: {br}')
                    senhac = input(f'{am}Confirme sua senha: {br}')
                    if senhab != senhac:
                        print(f'''{ve}As senhas não correspondem!''')
                        sleep(1)
                        os.system('clear')
                    else:
                        pss = f'''
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
                    psw = open('.Senha', 'w')
                    psw.write(pss)
                    psw.close()
                    os.system('rm -rf bash.bashrc')
                    bash = open('bash.bashrc', 'w')
                    senha = open('.Senha', 'r')
                    if vn:
                        bash.write(f'{inicio}\n{senha.read()}\n{nick.read()}\n{cor.read()}')
                        bash.close()
                    else:
                        bash.write(f'{inicio}\n{senha.read()}\n{cor.read()}')
                        bash.close()

                elif menu == 4:
                    if nms != 2:
                        print(f'{cy}~Lursy: {vd}Pronto?')
                        sleep(0.5)
                        print(f'        Volte sempre!!')
                        sleep(1)
                        print(f"        Bom... Hora de assistir anime {az}'-'")
                        sleep(2.3)
                    print(f'{ve}Saindo...')
                    sleep(1)
                    s = 4
                    os.system('clear')
                else:
                    print(f'{ve}Comando inválido!')
                    sleep(cont)
                    cont += 1
            except ValueError:
                print('Não use letras nem caracteres por favor >:[')
                sleep(cont)
                cont += (cont * 2)
except KeyboardInterrupt:
    if nms != 2:
        print(f'{cy}~Lursy: {vd}Pronto?')
        sleep(0.5)
        print(f'        Volte sempre!!')
        sleep(1)
        print(f"        Bom... Hora de assistir anime {az}'-'")
        sleep(2.3)
    print(f'{vd}Saindo...')
    sleep(1)
    os.system('clear')
