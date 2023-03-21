import time

vitoria = False

# Usa o tempo atual como semente para a geração de números aleatórios
seed = time.time()
seed = int((seed - int(seed)) * 1000000)

# Função para gerar números aleatórios
def generate_random_number(seed, min_val, max_val):
    a = 1103515245
    c = 12345
    m = 2**31
    seed = (a * seed + c) % m
    return min_val + (max_val - min_val) * seed / m

# Gera um número aleatório dentro do intervalo especificado
min_val = 0
max_val = 99
random_number = generate_random_number(seed, min_val, max_val)

while vitoria == False:
    num = int(input("Digite um número: "))
    if (num == int(random_number)):
        vitoria = True
    elif (num > random_number):
        print(f'O número sorteado é menor que {num}')
    else:
        print(f'O número sorteado é maior que {num}')

print(f'\n\nParábens!!!\nO número sorteado era {random_number:.0f}')