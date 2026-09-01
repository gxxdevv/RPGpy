import sys
from data.armas import armas
from data.itens import itens_gerais
from systems.personagem import heroi
from systems.inventario import mochila
from utils.interface import (
    escolher,
    confirmar,
    limpar_tela,
    efeito_digitacao,
    efeito_drama)


def tutorial():
    limpar_tela()
    pass

def personagem():
    while True:
        limpar_tela()
        print("\n===PERSONAGEM===")
        print(f"nome: {heroi['nome']}")
        print(f"força: {heroi['força']} ")
        print(f"hp: {heroi['hp']}")
        print(f"ouro: {heroi['ouro']}")
        print("===================")
        print("\n===MOCHILA===")
        for i, item in enumerate(mochila, start=1):
            print(f"{i}°- {item} ")
        print("================")
        
        opcao_perso = input("Deseja sair? (sim/não): ").strip().lower()
        
        if opcao_perso == "sim":
            break

def hacks():
    remover_item = False
    while True:
        limpar_tela()
        print("\n===𝖒𝖊𝖓𝖚 𝖉𝖊 𝖍𝖆𝖈k𝖘===")
        print("Aqui pode melhorar o que quiser!")
        escolha = escolher([
            "1- vida",
            "2- ouro",
            "3- força",
            "4- adicionar item a mochila",
            "5- remover item da mochila",
            "6- sair"
        ], "escolha uma opção")
        
        
        if escolha == "1- vida":
                limpar_tela()
                print(f"Quantide de vida atual: {heroi['hp']}")

                while True:
                    try:
                        opcao_hp = int(input("Qual quantidade de vida deseja agora? "))
                    except ValueError:
                        print("Digite apenas números!")
                        continue

                    heroi["hp"] = opcao_hp
                    print(f"Nova Quantidade de vida: {heroi['hp']}")
                    break

        elif escolha == "2- ouro":
                limpar_tela()
                print(f"Quantidade de ouro atual: {heroi['ouro']}𝖆𝖚")

                while True:
                    try:
                        opcao_ouro = int(input("Quanto ouro deseja? "))
                    except ValueError:
                        print("Digite apenas números!")
                        continue

                    heroi["ouro"] = opcao_ouro
                    print(f"Qauntidade de ouro atualizado: {heroi['ouro']}𝖆𝖚")
                    break

        elif escolha == "3- força":
                limpar_tela()
                print(f"Força atual: {heroi['força']}")
            
                while True:
                    try:
                        opcao_forca = int(input("Qual quantidade de força deseja agora? "))
                    except ValueError:
                        print("Digite apenas números!")
                        continue

                    heroi["força"] = opcao_forca
                    print(f"Força atualizada: {heroi['força']}")
                    break

        elif escolha == "4- adicionar item a mochila":
            while True:
                limpar_tela()
                print("\n=====MOCHILA=====")
                print("Digite o item que quer por na machila")
                print("==================")

                print("\n===Armas===")
                for i, arma in enumerate (armas, start=1):
                    print(f"{i}°- {armas[arma]["nome"]}")
                print("============")

                print("\n===Itens===")
                for i, item in enumerate (itens_gerais, start=1):
                    print(f"{i}°- {itens_gerais[item]["nome"]}")
                print("============")

                opcao_mochila = input("Qual item deseja adicionar em sua mochila? ").lower().strip()

                if opcao_mochila not in armas and opcao_mochila not in itens_gerais:
                    limpar_tela()
                    print("[ERRO]! Item não existe nesse universo")
                    opcao_hack = input("aperte enter para prosseguir")
                    if opcao_hack == "":
                        continue
                    
                else:
                    mochila.append(opcao_mochila)
                    print(f"O item '{opcao_mochila}' foi adicionado em sua mochila")
                        
                    if not confirmar("deseja por mais um item na sua mochila? "):
                        print("Ok, adeus")
                        break

        elif escolha == "5- remover item da mochila":
            while True:
                limpar_tela()
                print("\n===ITENS NA MOCHILA===")
                for i, item in enumerate(mochila, start=1):
                    print(f"{i}°- {item}")
                print("\n======================")
                
                opcao_remov = input("Qual item deseja remover? (escreva)").strip().lower()
                if opcao_remov not in mochila:
                    print("Esse item na está na sua mochila")
                else:
                    mochila.remove(opcao_remov)
                    print(f"{opcao_remov}, foi removido")
                    remover_item = True
                    break
                
        elif escolha == "6- sair":
                print("Saindo...")
                break

def novo_jogo():
    limpar_tela()
    print("\n===𝖍𝖎𝖘𝖙ó𝖗𝖎𝖆 𝖉𝖔 𝖏𝖔𝖌𝖔===")

    frase = "Seu jovem animal de estimação sofreu uma maldição..." \
        "Suba no topo do mundo para pegar um artefato que expurgará a maldição..." \
        "Salve seu amigo."
    efeito_digitacao(frase)

    opcao_new_game = input("Aperte 'enter' para prosseguir")
    if opcao_new_game == "":
        jogar_novo()

def jogar_novo():
    limpar_tela()
    print("OBS:SEMPRE APERTE 'ENTER' PARA PROSSEGUIR")
    opcao_jogo = input("Aperte 'enter' para prosseguir")
    if opcao_jogo == "":
        while True:
            limpar_tela()
            frase_jogo = "Jyota...Jyota... Acorde garoto!"
            efeito_digitacao(frase_jogo)
            continuar_jogo = input("")

            if continuar_jogo == "":
                frase_jogo = "JYOTA!"
                efeito_digitacao(frase_jogo)
                continuar_jogo = input("")
            
            if continuar_jogo == "":
                frase_jogo = "..."
                efeito_digitacao(frase_jogo)
                frase_jogo = "..."
                efeito_digitacao(frase_jogo)
                continuar_jogo = input("")
            
            if continuar_jogo == "":
                frase_jogo = f"{heroi['nome']}: O quê?! Que- Quem é você??? "
                efeito_drama(frase_jogo)
                continuar_jogo = input("")   
                break

def continue_game():
    limpar_tela()
    pass

def configuracoes():
    while True:
        limpar_tela()
        print("\n===𝕮𝖔𝖓𝖋𝖎𝖌𝖚𝖗𝖆çõ𝖊𝖘===")
        print("Olá jogador(a)... Bem-vindo ao seu menu de hacks")
        print("Sim, aqui você pode upar seu personagem ao nível máximo")
        print("Jogar assim é muito sem graça. Tente usar essas opções somente após zerar.")
        print("===================")

        escolha = escolher([
            "1- Menu de hacks",
            "2- Menu inicial"
        ], "escolha uma opção")
        
        
        if escolha == "1- Menu de hacks":
            hacks()
        elif escolha == "2- Menu inicial":
            print("Boa escolha!")
            break

def menu_inicial():
    while True:
        limpar_tela()
        print("\n===𝕽𝕻𝕲===")
        escolha = escolher([
            "1- novo jogo",
            "2- continuar jogo salvo",
            "3- configurações",
            "4- tutorial",
            "5- ver personagem",
            "6- sair do jogo"
        ], "escolha uma opção")
        
        
        if escolha == "1- novo jogo":
            novo_jogo()

        elif escolha == "2- continuar jogo salvo":
            continue_game()

        elif escolha == "3- configurações":
            configuracoes()

        elif escolha == "4- tutorial":
            tutorial()

        elif escolha == "5- ver personagem":
            personagem()
        
        elif escolha == "6- sair do jogo":
            frase_menu = "𝕺𝖇𝖗𝖎𝖌𝖆𝖉𝖔 𝖕𝖔𝖗 𝖏𝖔𝖌𝖆𝖗!"
            efeito_digitacao(frase_menu)
            sys.exit()

if __name__ == "__main__":
    menu_inicial()