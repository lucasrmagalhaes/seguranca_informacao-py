import ipaddress

ip = "192.168.0.1"
ip_rede = "192.168.0.0/24"

endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(ip_rede, strict = False)

print(f'Endereço: {endereco}')

for ip_rede in rede:
    print(f'Rede: {ip_rede}')