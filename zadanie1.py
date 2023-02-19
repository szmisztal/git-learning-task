print("Lista zakupów:")

lista_zakupów = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

for key, value in lista_zakupów.items():
    value = str(value)
    print("Idę do", key.capitalize(), "i kupuję tam", value.title())

ilość_produktów = (len(lista_zakupów['piekarnia'] + lista_zakupów['warzywniak']))
print("W sumię kupuję", ilość_produktów, "produktów")

print("abcd")