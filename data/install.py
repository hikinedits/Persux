from data.ferramentas import vd, ve
import os


def install():
    global nms
    os.chdir('/data/data/com.termux/files/home/')
    Ver = os.path.exists('.usuario')
    if not Ver:
        os.system('clear')
        user = str(input(f'{vd}Nome: {ve}'))
        os.system('clear')
        os.system('pkg install figlet -y')
        os.chdir('/data/data/com.termux/files/usr/etc/')
        os.system('rm -rf .Cor')
        cor = open('.Cor', 'w')
        cor.write(f"PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
        cor.close()
        os.system('rm -rf motd')
        os.chdir('/data/data/com.termux/files/home/')
        user_file = open('.usuario', 'w')
        user_file.write(user)
        user_file.close()
        os.system('clear')
        nms = 1
