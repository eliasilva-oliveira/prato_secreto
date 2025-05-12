import random

print("Bem vindo ao jogo numero secreto!")
print("\nEscolha o nível de dificuldade:")
print("1 - Fácil (30 tentativas)")
print("2 - Médio (15 tentativas)")
print("3 - Difícil (5 tentativas)")

secret_number = random.randint(10,100) 
tentativas = 0
pontuacao = 100

nivel = int (input("Digíte o número do nível:"))
if nivel == 1:
    tentativas = 30
    penalidade = -10
elif nivel == 2:
    tentativas = 15
    penalidade = -20
elif nivel == 3:
    tentativas = 5
    penalidade = -50

tentativa = 1
for tentativa in range(1, tentativas+1 ):
    print(f"\nTentativa {tentativa} de {tentativas}")
    print(f"Pontuação atual: {pontuacao}")
    palpite = int(input("Digíte um numero entre 10 e 100:"))
    if palpite < 10 or palpite > 100:
        print("O número deve estar entre 10 e 100!")
        continue
    if palpite == secret_number:
        print("Parabéns!! Você acertou!")
        break
    elif palpite < secret_number:
        print("O valor informado é menor que o numero secreto.")
        pontuacao += penalidade
    elif palpite > secret_number:
        print("O valor informado é maior que o numero secreto.")
        pontuacao += penalidade
    else:
        print("Valor desconhecido")









