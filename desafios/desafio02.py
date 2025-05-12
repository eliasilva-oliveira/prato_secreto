valor = int(input("Informe um valor entre 10 e 100:"))

if valor < 10 or valor > 100:
    print("Valor inválido")
else:
    for i in range(valor+1):
        print(f"Contando: {i}")