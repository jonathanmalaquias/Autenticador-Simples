#!/usr/bin/env python
# coding: utf-8

# In[ ]:


########## importando get pass da biblioteca pra ninguem saber oque estamos fazendo 🤫, usar o timer para a espera de novas tentavivas

import getpass
import time #novidade :D
import os

########### variáveis globais :), tenho que parar de usar apenas elas e começar a usar return

continuar_programa = True
senha = ""
tentativas = 3

########## " Menu principal " 

def inicio():
    limpar_tela()
    global tentativas
    if senha == "" :
        print("Nenhuma senha definida")
        novasenha()
    else :
        print("Olá oque deseja fazer ?")
        print(" 1 Logar, 2 Fechar")
        escolha = input(" Digite ->")
        if escolha == "1" :
            if tentativas == 0:
                print("\n--- SISTEMA BLOQUEADO ---")
                for i in range(10, 0, -1):
                    print(f"Aguarde {i} segundos para o reset...", end="\r")
                    time.sleep(1)
                tentativas = 3
                print("\nTentativas restauradas! Pode tentar logar novamente.")
            else:
                logar()
        elif escolha == "2" :
            print("Fim do progrma, Obrigado por usar :)")
            return "parar"
        else :
            print("Comando não indentificado")
########## func para comparar a senha com a tentativa

def logar():
    global tentativas
    print("Para logar digite sua senha abaixo:")
    tentativa = getpass.getpass("senha ->")
    if tentativa != senha :
        tentativas -= 1
        print(f"Senha errada!, tentativas restantes:{tentativas}")
    elif tentativa == senha :
        print("Acesso permitido")
        print(" o__            o/      | |\   ")
        print("/|              /\      | |X\  ")
        print("/ > o            <\     | |XX\ ")
        print("Oque deseja fazer?")
        print("1 Mudar Senha, 2 Sair")
        escolha = input("->")
        if escolha == "1":
            novasenha()
        elif escolha == "2":  
            pass #aqui usei o pass pois me pareceu melhor opção doque chmar o inicio() de novo

########## func para definir a primeira senha e para muda-la 

def novasenha():
    global senha
    print("Defina sua nova Senha")
    senha = getpass.getpass("Senha ->")
    print("Nova senha Definida com sucesso")

######### func pra limpar o terminal/prompt

def limpar_tela():
    # Se for Windows, usa 'cls'. Se for Linux/Mac, usa 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')

###### loop

while continuar_programa == True:
    comando = inicio()
    if comando == "parar":
        break


# In[ ]:




