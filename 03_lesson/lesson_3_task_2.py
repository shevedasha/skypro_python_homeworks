from smartphone import Smartphone

catalog = []

phone_1 = Smartphone('Vivo', 'S12', '+79221824007')
phone_2 = Smartphone('Honor', 'S11', '+79221824006')
phone_3 = Smartphone('Xiaomi', 'S10', '+79221824005')
phone_4 = Smartphone('Infinix', 'S9', '+79221824004')
phone_5 = Smartphone('Oppo', 'S7', '+79221824003')

catalog.append(phone_1)
catalog.append(phone_2)
catalog.append(phone_3)
catalog.append(phone_4)
catalog.append(phone_5)

for phone in catalog:
    print(f"{phone.marka} - {phone.model}. {phone.number}")
