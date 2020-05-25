import os

os.system("clear")

def lin():
    print('/' * 74)


lin()
print("""
  _   __  ___   _      _____          _____ ______   ___   ________   __
 | | / / / _ \ | |    |_   _|        /  __ \| ___ \ / _ \ |___  /\ \ / /
 | |/ / / /_\ \| |      | |   ______ | /  \/| |_/ // /_\ \   / /  \ V / 
 |    \ |  _  || |      | |  |______|| |    |    / |  _  |  / /    \ /  
 | |\  \| | | || |____ _| |_         | \__/\| |\ \ | | | |./ /___  | |  
 \_| \_/\_| |_/\_____/ \___/          \____/\_| \_|\_| |_/\_____/  \_/  
                                                     Creat by Crazy!                   
""")
lin()

option = input('Type anything to leave or press enter to continue ...')
if option == "":
    try:
        os.system("curl -LO https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter")
        os.system("chmod +x kalinethunter")
        os.system("./kalinethunter")
    except:
        print('ERRO')
    else:
        os.system("statkali")
else:
    os.system("clear")
