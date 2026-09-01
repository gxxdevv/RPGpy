from InquirerPy import prompt
import time
import os

def escolher(opcoes, mensagem = "escolha uma opção:"):
    escolhas = [{
        "type": "list",
        "name": "escolha",
        "message": mensagem,
        "choices": opcoes
    }]
    
    resultado = prompt(escolhas)
    return resultado["escolha"]

def confirmar(pergunta):
    while True:
        resposta = input(f"{pergunta} (sim/não): ").strip().lower()
        
        if resposta in ["sim", "s", "ss"]:
            return True

        if resposta in ["não", "nao", "n", "nn"]:
            return False
        print("digite sim ou não")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def efeito_digitacao(text, delay=0.05):
        for letra in text:
            print(letra, end="", flush=True)
            time.sleep(delay)
        print()

def efeito_drama(text, delay=0.1):
    for letra in text:
        print(letra, end="", flush=True)
        time.sleep(delay)
    print()