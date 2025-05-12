frutas = ["maçã", "banana", "laranja", "pera", "abacaxi"]

print(frutas[2])
print(frutas[-1])
print(frutas[-2])
print(frutas[0:2])
print(frutas[1:3])
print(frutas[:])
print(frutas[::2])

#Tamanho len()
print(len(frutas))

#concatenar - juntar (+)
mais_frutas = ["morango", "uva"]
cesta_de_Frutas = frutas + mais_frutas
print(cesta_de_Frutas)

#Repetir o array
repita = frutas * 3
print(repita)

#Adicionar elementos
frutas.append("goiaba")
print(frutas)

#Adiciona um elemento numa posição especifica
frutas.insert(0,"melao")
print(frutas)

frutas_dois = ["tomate", "kiwi"]
frutas.extend(frutas_dois)
print(frutas)
frutas.insert(2,frutas_dois)
print(frutas)

#Remover dados da lista
frutas.remove("melao")
print(frutas)

elemento = frutas.pop(2)
print(frutas)#Exibe o array sem o elemento retirado pelo pop
print(elemento)#Exibe somente o elemento

