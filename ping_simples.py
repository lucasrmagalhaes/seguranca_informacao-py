# Importa o módulo ou bliblioteca os (integra os programas e recursos do S.O.
import os

# Imprimindo # 60 vezes
print("#" * 60)

# Variável que vai receber do usuário um IP
ip_ou_host = input("Digite o IP ou host: ")

# Imprimindo - 60 vezes
print("-" * 60)

# Chamando system da biblioteca os - comando ping
# -n -num de pacotes que serão 6 {}
os.system('ping -n 6 {}'.format(ip_ou_host))

# Imprimindo - 60 vezes
print("-" * 60)