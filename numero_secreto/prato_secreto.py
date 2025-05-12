import random

pratos = ["lasanha", "strogonoff", "feijoada", "pizza"]
prato_secreto = random.choice(pratos)

print("Bem-vindo ao jogo Prato Secreto!")
print("Você tem 5 tentativas para adivinhar o prato.")

tentativas = 5

for tentativa in range(1, tentativas + 1):
    palpite = input(f"Tentativa {tentativa}: Qual é o seu palpite? ").lower().strip()

    if palpite == prato_secreto:
        print("Parabéns! Você acertou o prato secreto!")
        break
    else:
        tentativas_restantes = tentativas - tentativa
        if tentativas_restantes > 0:
            print(f"Você errou! Ainda tem {tentativas_restantes} tentativa(s).")
        else:
            print(f"Fim de jogo! O prato secreto era {prato_secreto}.")



