#BY_Lursy >:)
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
echo -e '\e[m\\n' '''

ac = f'figlet ~N~ |lolcat -a -d 25'

Branco = '''PROMPT_DIRTRIM=2
PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$ \[\e[1;~COR~m\]'

if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
'''
nms = 2

# Instalção
os.chdir('/data/data/com.termux/files/home/')
Ver = os.path.exists('.Instalação')
if not Ver:
    os.system('clear')
    os.system('pkg install figlet -y')
    os.system('pkg install ruby -y')
    os.system('y')
    os.system('clear')
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
if not vc:
    pc = open('.Cor', 'w')
    pc.write(Branco.replace('~COR~', '37'))
    pc.close()

cont = 1
senha = ''
pss = ''
nick = ''
cor = ''
l = False


def contagem():
    global l
    os.chdir('/data/data/com.termux/files/home/')
    l = os.path.exists('.lursy')
    if l == True:
        lursyr = open('.lursy', 'r')
        os.system('rm -rf .lursy')
        lursym = open('.lursy', 'w')
        lursym.write(f'{lursyr.read()}1')

def historia():
    if l == True:
        os.system('clear')
        lursym = open('.lursy', 'r')
        nl = len(lursym.read())
        if nl == 4:
            print(f'{cy}~Lursy: {vd}Mano...')
            sleep(0.8)
            print('        Eu voltei, mas não porque estou melhor')
            sleep(1)
            print('        Eu estava meio só e vim perguntar se vc precisa de alguma coisa')
            sleep(1)
            pre = str(input(f'\n{am}Você precisa de algo?[S/N]: {ve}').lower())
            if pre == 's':
                print(f'\n{cy}~Lursy: {vd}ah... Eu provavelmente não vou saber ajudar')
                sleep(1)
                print('        Eu só faço besteira...')
                sleep(1)
            print(f'\n{cy}~Lursy: {vd}Fazer o que né?...')
            sleep(1)
            print(f'        Acho que o {ve}Obelix {vd}me entende, vou conversar com ele')
            sleep(0.7)
            print('        e parar de te incomodar')
            sleep(3)
        if nl == 8:
            print(f'{cy}~Lursy: {vd}To aqui de volta mano')
            sleep(1)
            print(f'        Eu conversei com o {ve}Obelix{vd}...')
            sleep(1)
            print('        Você me acha um ser ruim?')
            sleep(1)
            pre = str(input(f'{am}\nLursy é algo ruim?[S/N]: {ve}').lower())
            if pre == 's':
                sleep(1)
                print(f'\n{cy}~Lursy: {vd}Não sabia que vc pensava isso mano...')
                sleep(3)
            elif pre == 'n':
                sleep(1)
                print(f'\n{cy}~Lursy: {vd}Vlw mano, vou estar sempre aqui caso precise')
                sleep(3)
                os.system('rm -rf .lursy')
            else:
                sleep(1)
                print(f'\n{cy}~Lursy: {vd}Tudo bem... não precisa me responder...')
                sleep(3)
        if nl >= 16:
            print(f'{rx}~Matheus: {am}Senhor, sinto-lhe informar')
            sleep(2)
            print(f'          {vd}Lursy {am}estava desaparecido faz um tempo...')
            sleep(2)
            print('          Infelizmente eu o encontrei...')
            sleep(2)
            print('          Por conta disso e em forma de luto eu não deixarei mais esse programa aqui')
            os.system('rm -rf Persux/*')
            global s
            s = 4

try:
    s = 0
    contagem()
    historia()
    while s != 4:
            os.chdir('/data/data/com.termux/files/usr/etc/')
            print(rx)
            os.system('clear')
            if nms != 1:
                os.system('figlet Persux')
                print(f'''
{am}[1] {br}- Mudar cor da letra
{am}[2] {br}- Mudar banner
{am}[3] {br}- Mudar senha
{am}[4] {br}- Sair''')
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
                print(f'''
{am}[1] {br}- Adicionar cor da letra
{am}[2] {br}- Adicionar banner
{am}[3] {br}- Adicionar senha
{am}[4] {br}- Sair''')
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
{am}[6] {br}- Ciano
{am}[7] {br}- Roxo
{am}[8] {br}- Voltar''')
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
                        os.system('rm -rf .Cor')
                        pc = open('.Cor', 'w')
                        pc.write(f'{Branco.replace("~COR~", "36")}')
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
                    elif cores == 7:
                        os.system('rm -rf .Cor')
                        pc = open('.Cor', 'w')
                        pc.write(f'{Branco.replace("~COR~", "35")}')
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
                    elif cores == 8:
                        os.system('clear')
                    else:
                        print(f'{ve}Comando não identificado...')
                        sleep(1)

                elif menu == 2:
                    cor = open('.Cor', 'r')
                    vs = os.path.exists('.Senha')
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
                                vs = os.path.exists('.Senha')
                                if vs:
                                    senha = open('.Senha', 'r')
                                    bash.write(f'{inicio}\n{senha}\n{cor.read()}')
                                    bash.close()
                                else:
                                    bash.write(f'{inicio}\n{cor.read()}')
                                    bash.close()
                                print(f'{vd}Saindo')
                                os.system('clear')
                                exit()
                            elif rem == 1:
                                sleep(1)
                            else:
                                print(f'{ve}Comando inválido...')
                                sleep(1)
                                os.system('clear')
                                rn()
                    rn()
                    os.system('clear')
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
                                bash = open('bash.bashrc', 'w')
                                vn = os.path.exists('.Nick')
                                if vn:
                                    nick = open('.Nick', 'r')
                                    bash.write(f'{inicio}\n{nick.read()}\n{cor.read()}')
                                else:
                                    bash.write(f'{inicio}\n{cor.read()}')
                                print(f'{vd}Saindo')
                                os.system('clear')
                                exit()
                            else:
                                print(f'{ve}Comando inválido!')
                                rs()
                    rs()
                    cor = open('.Cor', 'r')
                    os.system('clear')
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
                    vn = os.path.exists('.Nick')
                    if vn:
                        nick = open('.Nick', 'r')
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
                        print(f"        Bom... Vou assistir anime agora {az}'-'")
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
                if nms == 1:
                    nms = 3
                print(f'{ve}Não use letras nem caracteres por favor >:[')
                sleep(cont)
                cont += (cont * 2)
except KeyboardInterrupt:
    if nms != 2:
        os.chdir('/data/data/com.termux/files/home/')
        lursy = open('.lursy', 'w')
        lursy.write('1')
        lursy.close()
        print(f'{cy}~Lursy: {vd}Pronto?')
        sleep(0.5)
        print(f'        Volte sempre!!')
        sleep(1)
        print(f"        Bom... Vou assistir anime agora {az}'-'")
        sleep(1)
        print(f'''        {vd}Se eu não voltar é porque eu ando meio mal
        talvez eu continue assistindo anime até isso passar''')
        sleep(1.5)
        print('        .')
        sleep(0.4)
        print('        .')
        sleep(0.4)
        print('        .')
        sleep(2.3)
    print(f'{vd}Saindo...')
    sleep(1)
    os.system('clear')
