print("Lista zakupów:")

shopping_list = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

for key, value in shopping_list.items():
    value = str(value)
    print("Idę do", key.capitalize(), "i kupuję tam", value.title())

how_many_products = (len(shopping_list['piekarnia'] + shopping_list['warzywniak']))
print("W sumię kupuję", how_many_products, "produktów")