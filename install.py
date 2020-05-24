import os

Pkg = str(input('Instalar as dependências ? [s/n]: ')).lower()

if Pkg == "s":
    try:
        os.system("pkg install termux-api -y")
        os.system("pkg install nmap -y")
        os.system("pkg install espeak -y")
        os.system("pkg install cowsay -y")
        os.system("pkg install sl -y")
        os.system("pip install requests")
        os.system("mv sbs ../../usr/bin")
        os.system("mv ~/botscan ../usr/etc")
    except:
        print("  HOUVE ALGUM ERRO OU O PROCESSO FOI MORTO!")
    else:
        print("\n\033[1;32mDependências instaladas com sucesso!\033[m")
elif Pkg == "n":
    exit()
else:
    print("Digite S ou N, seu animal!")
