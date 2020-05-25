import os

try:
    os.system("mv srs ~/../usr/bin")
except:
    print("erro ao execultar tente manualmente!")
else:
    print("use o comando srs para iniciar")

