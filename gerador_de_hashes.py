import hashlib

string = input('Digite o texto a ser gerado a hash: ')

menu = int(input(''' #### MENU - ESCOLHA O TIPO DE HASH 
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print(f'O hash MD5 da string: {string} é: {resultado.hexdigest()}')
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print(f'O hash SHA1 da string: {string} é: {resultado.hexdigest()}')
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print(f'O hash SHA256 da string: {string} é: {resultado.hexdigest()}')
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print(f'O hash SHA512 da string: {string} é: {resultado.hexdigest()}')
else:
    print('Opção inválida.')