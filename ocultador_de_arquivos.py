import ctypes

# pasta = input("Digite o caminho da pasta a ser ocultada: ")

atributo_ocultar = 0x02

# retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)
retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultador_de_arquivos_arquivo.txt', atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado.")
else:
    print("Arquivo não foi ocultado.")