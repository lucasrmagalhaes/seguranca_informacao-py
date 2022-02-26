import random, string

# tamanho = 16
tamanho = int(input('Digite o tamanho da senha: '))

chars = string.ascii_letters + string.digits + 'ç!@#$%&*'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))