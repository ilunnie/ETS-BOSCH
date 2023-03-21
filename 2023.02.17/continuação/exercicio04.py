lista = []

for i in range(10):
    lista.append(float(input(f"Digite o {i+1}° valor: ")))

print(f"A lista tem {len(lista)} valores")
lista.sort()
print(lista)