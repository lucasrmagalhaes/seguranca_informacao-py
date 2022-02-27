import os
import time

hosts = 'ping_multiplo_hosts.txt'

with open(hosts) as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o IP: ', ip)
        print('-' * 60)
        os.system('ping -n 2 {}'.format(ip))
        print('-' * 60)
        time.sleep(5)