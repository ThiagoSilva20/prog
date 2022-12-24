preco_produtos = {
    "Motorola": 1950,
    "Iphone": 2100,
    "Asus": 1500,
    "Xiaomi": 2000
}

# normal

imposto_01 = []

for produto in preco_produtos:
    imposto_01.append(preco_produtos[produto] * 0.1)

# print(imposto_01)

# list comprehension

imposto_02 = [preco_produtos[produto] * 0.1 for produto in preco_produtos ]
print(imposto_02)
