from functools import reduce

produtos = [
    {"nome": "Arroz", "preco": 20.0, "categoria": "Alimentos"},
    {"nome": "Feijão", "preco": 10.0, "categoria": "Alimentos"},
    {"nome": "Shampoo", "preco": 15.0, "categoria": "Higiene"},
    {"nome": "Sabão", "preco": 5.0, "categoria": "Higiene"},
]

produtos_com_desconto = list(map(
    lambda p: {**p, "preco": round(p["preco"] * 0.9, 2)}, produtos
))

alimentos = list(filter(lambda p: p["categoria"] == "Alimentos", produtos_com_desconto))

total = reduce(lambda acc, p: acc + p["preco"], alimentos, 0)

print("Produtos com desconto:", produtos_com_desconto)
print("Apenas alimentos:", alimentos)
print("Total de alimentos:", total)
