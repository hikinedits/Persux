from data.ferramentas import *


def install():
    global nms
    os.chdir('/data/data/com.termux/files/home/')
    Ver = os.path.exists('user')
    if not Ver:
        os.system('clear')
        user = str(input(f'{vd}Nick: '))
        os.system('clear')
        os.system('pkg install figlet -y')
        os.chdir('/data/data/com.termux/files/usr/etc/')
        os.system('rm -rf motd')
        os.chdir('/data/data/com.termux/files/home/')
        user_file = open('user', 'w')
        user_file.write(user)
        user_file.close()
        os.system('clear')
        nms = 1
