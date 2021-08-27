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

banner_nick = '''echo -e '\e[0;:corm'
figlet :name
echo -e '\e[m\\n' '''

ac = f'figlet ~N~ |lolcat -a -d 25'

user = (open('.usuario', 'r')).readline()[:-1]

cor_letra = f'''PROMPT_DIRTRIM=2
PS1='\[\e[0;31m\]┏(\[\e[0;34m\]{user}\[\e[0;31m\]) [\[\e[0;32m\]\w\[\e[0;31m\]] \\n\[\e[0;31m\]┗► \[\e[1;:corm\]'
'''
final ='''if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
'''


error = 0
cont = 1
pss = nick = cor = senha = ''
os.chdir('/data/data/com.termux/files/usr/etc/')
vc = os.path.exists('.Cor')


def pacote():
    if not vc:
        pc = open('.Cor', 'w')
        pc.write(cor_letra.replace('~COR~', '37'))
        pc.close()
