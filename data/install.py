from data.ferramentas.cores import *


def install():
    global nms
    os.chdir('/data/data/com.termux/files/home/')
    Ver = os.path.exists('.usuario')
    if not Ver:
        os.system('clear')
        user = str(input(f'{vd}Nick: {ve}'))
        os.system('clear')
        os.system('pkg install figlet -y')
        os.chdir('/data/data/com.termux/files/usr/etc/')
        os.system('rm -rf .Cor')
        cor = open('.Cor', 'w')
        cor.write(f'{cor_letra.replace(":cor", "37")}')
        cor.close()
        os.system('rm -rf motd')
        os.chdir('/data/data/com.termux/files/home/')
        user_file = open('.usuario', 'w')
        user_file.write(user)
        user_file.close()
        os.system('clear')
        nms = 1
