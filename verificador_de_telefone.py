import phonenumbers 
from phonenumbers import geocoder

phone = input('Digite o telefone no formato +5551986114511: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))

# Rio Grande do Sul