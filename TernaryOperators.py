vendas = 1500

meta = 1000

# if vendas >= meta:
#     bonus = 30
#     vendas += bonus
# else: 
#     bonus = 0

# print(vendas)

# ternary operator
bonus_02 = 30 if vendas >= meta else 0 
print("Suas vendas mais o bonus atingido pela meta equivalem: ", vendas + bonus_02)