import os
import requests
from time import sleep

color = {'end':'\033[m', 'red':'\033[1;31m', 'green':'\033[1;32m', 'yellow':'\033[1;33m', 'cyan':'\033[1;36m'}


##############banner###########################
#def do banner
def banner():
    print("""{}
____________________________
< Robot Scan creat by Crazy© >
 ----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||
            {}""".format(color['cyan'], color['end']))
    print('{}∆{}'.format(color["green"], color["end"]) * 50)
    os.system("termux-tts-speak Olá, seja bem vindo ao, Robot Scan")


###################ligin#######################
def login():
    print("ROBOT SCAN CREAT BY CRAZY")
    os.system("espeak robot-scan-creat-by-crazy")
    os.system("cowsay AGUARDE, A SESSÃO  ESTÁ SENDO INICIADA")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    os.system("termux-tts-speak aguarde, a sessão está sendo iniciada")
    print("5")
    sleep(1)
    print("4")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    os.system("sl")
    os.system("sessão iniciada com sucesso")
    os.system("clear")


######################ping_host#################
#def do ping
def ping_host():
    os.system("cowsay digite o resto do link")
    os.system("termux-tts-speak digite o resto do link")
    host = input("https://")
    os.system("termux-tts-speak não precisa usar control c. por favor, espere")
    print('NÃO USE CTRL+C ELE VAI PARAR SOZINHO, ESPERE!...')
    sleep(3)
    os.system("ping -c 1 {}".format(host))


#################nmap_param####################
#def no nmap com parâmetro escolhido pelo usuário
def nmap_param():
    ip_url = input('Cole ou digite o HOST ou IP: ')
    param = input("Digite o parâmetro que deseja: ")
    os.system("nmap {0} {1}".format(param, ip_url))


##############nmap_0###########################
#def do nmap simples                                                          
def nmap_0():
    url = input('Digite ou cole o ip ou link do alvo: ')
    os.system("nmap {}".format(url))



################instaled#######################
#def de instalação das dependências (caso o usuário não tenha)
def instaled():
    PkgInstall = str(input('Deseja instalar as dependências nessesárias? [s/n]: ')).lower() 
    if PkgInstall == "s":
        try:
            os.system("pkg install termux-api -y ; pkg install nmap -y ; pkg install espeak -y ; pkg install cowsay -y ; pkg install sl -y ; pip install requests")
        except:
            print("  HOUVE ALGUM ERRO OU O PROCESSO FOI MORTO!")
    elif PkgInstall == "n":
        os.system("clear")
    else:
        print("Digite S ou N, seu animal!")


##################tutorial#####################
def tutorial():
    try:
        print("""
1-Português
2-English
        """)
        idioma = int(input('What is your idiom?\nQual é seu idioma? '))
        
        if idioma == 1:
            os.system("cowsay A opção 0 te expulsa do programa, a opção 1 serve para pegar o ip do site alvo usando o comando ping, 2 use o nmap com um parâmetro passado por você, 3 escaneamento simples com o nmap, 4 use o kuests, um script criado por mim para facilitar o uso do requests, 5 Tutorial em alta voz.")
            os.system("termux-tts-speak A opção 0 te expulsa do programa, a opção 1 serve para pegar o ip do site alvo usando o comando ping, 2 use o nmap com um parâmetro passado por você, 3 escaneamento simples com o nmap, 4 use o kuests, um script criado por mim para facilitar o uso do requests, 5 Tutorial em alta voz.")

        elif idioma == 2:
            os.system("cowsay Option 0 expels you from the program, option 1 is to get the ip of the target site using the ping command, 2 use nmap with a parameter passed by you, 3 simple scan with nmap, 4 use kuests, a script created  by me to facilitate the use of requests, 5 Tutorial in loud voice.")
            os.system("espeak Option-0-expels-you-from-the-program,-option-1-is-to-get-the-ip-of-the-target-site-using-the-ping-command,-2-use-nmap-with-a-parameter-passed-by-you,-3-simple-scan-with-nmap,-4-use-kuests,-a-script-created-by-me-to-facilitate-the-use-of-requests,-5-Tutorial-in-loud-voice.")


    except:
        print('escolha 1 ou 2 seu desprovido de neurônio')


####################kuest######################
def kuest():
    cor = {'end':'\033[m', 'yellow':'\033[1;33m', 'green':'\033[1;32m'}
    color = {'red' : '\033[31m', 'fim' : '\033[m'}
    banner = {"b":'\033[1;36;40m'}

    def lin():
        print('{}==={}'.format(color['red'], color['fim']) *20)
	
	
    lin()
    print("""
	 {0}_  _ _  _ ____ ____ ___ ____ {3} 
	 {1}|_/  |  | |___ [__   |  [__  {4}
	 {2}| \_ |__| |___ ___]  |  ___] {5}
	 """.format(banner['b'], banner['b'], banner['b'], color['fim'], color['fim'], color['fim']))
    lin()
	
    print('Desenvolvido por {}Crazy{}!'.format(banner['b'], color['fim']))
	
	
    #escolha do usuário
    opcao = input("""{}
Escolha o número da opção junto\ncom a letra do que você quer.\nExemplo: 1a.
	
_______________________________________________________
[1]get            |
  a).text         |  Imprime o html do site.
  b).encoding     |  Ver a codificação.
  c).encodin=" "  |  Muda a codificação.
  d).content      |  acessa a resposta do servidor.
  e).status_coding|  Ver o código de status.
  f).headers      |  Mostra o cabeçalho do servidor.
  g).cookies      |  Mostra os cookies (se tiver).
  h).json()       |
[2] sem conteúdo
[3] sem conteúdo
[4] sem conteúdo
	
{}{}K》>{}""".format(cor["green"], cor["end"], cor["yellow"], cor["end"]))
    try:
        #se a escolha for 1a (text)
        if opcao == "1a":
            try:
                url = input('1a_cole o site: ')
                r = requests.get(url)
                print('\nAnalizando html do site...\n')
                sleep(2)
            except:
                print('{}ERRO{}1a'.format(color['red'], color['fim']))
            else:
                print(r.text)
        
        #caso a escolha seja 1b (encoding)
        elif opcao == "1b":
            try:
                url = input('1b_cole o site: ')
                r = requests.get(url)
                print('espere')
                sleep(1)
            except:
                print('{}ERRO{}1b!'.format(color['red'], color['fim']))
            else:
                print(r.encoding)

        #caso a escolha seja 1c (encoding=" ")
        elif opcao == "1c":
            try:
                url = input('1c_cole o site: ')
                r = requests.get(url)
                cod = input('Qual a codificação nova? ')
                print('calma...')
                sleep(1)
            except:
                print('{}ERRO{}1c!'.format(color['red'], color['fim']))
            else:
                r2 = r.encoding="{}".format(cod)
                print(r2)

        #caso a escolha seja 1d (content)
        elif opcao == "1d":
            try:
                url = input('1d_cole o site: ')
                r = requests.get(url)
                print('espera...')
                sleep(1)
            except:
                print('{}ERRO{}1d!'.format(color['red'], color['fim']))
            else:
                print(r.content)

        #caso a escolha seja 1e (status_code)
        elif opcao == "1e":
            try:
                url = input('1e_cole o link: ')
                r = requests.get(url)
                print('verificando status_code...')
                sleep(1)
            except:
                print('{}ERRO{}1e!'.format(color['red'], color['fim']))
            else:
                print(r.status_code)

        #caso a escolha seja 1f (headers)
        elif opcao == "1f":
            try:
                url = input('1f_cole o link: ')
                r = requests.get(url)
                print('procurando headers...')
                sleep(1)
            except:
                print('{}ERRO{}1f!'.format(color['red'], color['fim']))
            else:
                print(r.headers)

        #caso a escolga seja 1g (cookies)
        elif opcao == "1g":
            try:
                url = input('1g_cole o link: ')
                r = requests.get(url)
                print('procurando cookies...')
                sleep(1)
            except:
                print('{}ERRO{}1g!'.format(color['red'], color['fim']))
            else:
                print(r.cookies)

        #caso a escolha seja 1h (JSON())
        elif opcao == "1h":
            try:
                url = input('1h_cole o link: ')
                r = requests.get(url)
                print('verificando json...')
                sleep(1)
            except:
                print('{}ERRO{}1h!'.format(color['red'], color['fim']))
            else:
                print(r.json)

    except:
        print('erro')
	
