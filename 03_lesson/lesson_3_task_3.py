from Add import Address
from Mail import Mailing

to_address = Address('620440', 'Екатеринбург', 'Щербакова', '18', '20')
from_address = Address('621341', 'Серов', 'Кирова', '4', '30')
mailing = Mailing(to_address, from_address, 897, 'NBI124')

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f" {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f" {mailing.to_address.house} - {mailing.to_address.flat}. Стоимость {mailing.cost} рублей.")
 