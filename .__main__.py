import os
import botscan
from time import sleep
from random import randint

t = randint(0, 10)
os.system("clear")
color = {'end':'\033[m', 'red':'\033[1;31m', 'green':'\033[1;32m', 'yellow':'\033[1;33m', 'cyan':'\033[1;36m'}

####################CORPO-DO-PROGRAMA#####################

botscan.login()
os.system("clear")
botscan.banner()
os.system("termux-tts-speak você tem {} sessões para usar".format(t))
for c in range(0, t):
    try:
        print("""{}
        [0] Sair
        [1] Ping (esse serve para pegar o ip do site alvo)
        [2] Nmap [parâmetro] (escolha o parâmetro)
        [3] Nmap |host| (escaneamento simples)
        [4] Kuests (usa o requestes de modo simples.
        [5] Tutorial em alta voz.
        {}""".format(color['yellow'], color['end']))

        os.system("termux-tts-speak digite a opção que deseja usar")

        menu = int(input('{} scan{}{}>>{} '.format(color['cyan'], color['end'], color['yellow'], color['end'])))
    except:
        print('{}[!]Escolha um número seu animal.{}'.format(color['red'], color['end']))
        os.system("termux-tts-speak escolha um número seu animal")
    else:
        try:
            if menu == 0:
                print('Encerrando sessão...')
                sleep(3)
                os.system("clear")
                print('{}✓{}Seção encerrada com sucesso!'.format(color['green'], color['end']))
                print('{}ATÉ MAIS OTÁRIO!{}'.format(color["yellow"], color["end"]))
                os.system("espeak sessão-encerrada-com-sucesso...-até-mais-otário")
                break
            elif menu == 1:
                botscan.ping_host()
            elif menu == 2:
                botscan.nmap_param()
            elif menu == 3:
                botscan.nmap_0()
            elif menu == 4:
                botscan.kuest()
            elif menu == 5:
                botscan.tutorial()
            else:
                print('{}[!]Escolha de 0 a 6 seu animal seu animal!{}'.format(color['red'], color['end']))
                os.system("termux-tts-speak escolha um númer entre 0 e 6 seu animal")
        except:
            print("""
                {}ATENÇÃO{}""".format(color["red"], color["end"]))
            os.system("cowsay Algo deu errado! os motivos para isso acontecer são: matar o processo, erro na execulção, comando digitado errado ou você não instalou as dependências da opção 4. Se o erro continuar acesse a opção 4 e instale as dependências. Obrigado pela atenção e me pague um pc")
            os.system("termux-tts-speak Algo deu errado! os motivos para isso acontecer são: matar o processo, erro na execulção, comando digitado errado ou você não instalou as dependências da opção 4. Se o erro continuar acesse a opção 4 e instale as dependências. Obrigado pela atenção e me pague um pc")
