import os

print("[Gerenciador de atalhos]")
print("Escolha a página que deseja abrir")
while True:
    print("Youtube [1]")
    print("Google [2]")
    print("Github [3]")
    print("Sololearn [4]")
    print("Sair [5]")

    Option = int(input())
    if Option == 1:
        os.system('cmd /c start chrome "https://www.youtube.com/"')
    elif Option == 2:
        os.system('cmd /c start chrome "https://www.google.com.br/"')
    elif Option == 3:
        os.system('cmd /c start chrome "https://github.com/amostrawm"')
    elif Option == 4:
        os.system('cmd /c start chrome "https://www.sololearn.com/profile/10034312"')
    elif Option == 5:
        break
