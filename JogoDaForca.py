# Importa as bibliotecas necessárias
import os
import random

# Função para limpar o terminal
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal do jogo da forca
def jogar_forca():
    while True:
        # Gera uma palavra secreta aleatória
        palavra_secreta = obter_palavra_aleatoria()
        letras_acertadas = ''
        tentativas = 0

        while True:
            # Obtém uma letra do usuário
            letra_digitada = obter_letra()
            tentativas += 1

            # Verifica se a letra digitada está na palavra secreta
            if letra_digitada in palavra_secreta:
                letras_acertadas += letra_digitada

            # Obtém a palavra formada com as letras acertadas
            palavra_formada = obter_palavra_formada(palavra_secreta, letras_acertadas)
            print(palavra_formada)

            # Verifica se o jogador acertou a palavra
            if palavra_formada == palavra_secreta:
                limpar_terminal()
                print('Win! Você ganhou!')
                print(f'A palavra era "{palavra_secreta}"')
                print(f'Tentativas: {tentativas}')
                letras_acertadas = ''
                tentativas = 0

                # Pergunta se o jogador quer tentar novamente
                tentar_novamente = input('Digite qualquer tecla para continuar ou (N)ão encerrar: ')
                if tentar_novamente.lower() == 'n':
                    print('Encerrando...')
                    return
                else:
                    break

# Função para obter uma letra do usuário
def obter_letra():
    while True:
        letra_digitada = input('Digite uma letra: ')
        if len(letra_digitada) == 1 and letra_digitada.isalpha():
            return letra_digitada
        else:
            print('Digite apenas uma letra: ')

# Função para construir a palavra formada com as letras acertadas
def obter_palavra_formada(palavra_secreta, letras_acertadas):
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    return palavra_formada

# Função para obter uma palavra aleatória
def obter_palavra_aleatoria():
    palavras = ['rato', 'gato', 'cachorro', 'elefante', 'tigre', 'leão']
    return random.choice(palavras)

# Início do jogo da forca
jogar_forca()
