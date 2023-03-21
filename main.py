d1 = {
    'nome': 'Kenzinho',
    'cidade': 'Curitiba',
    'modulo': 'm5'
}

"""
    print(d1.get('nome'))
    print(d1.get('cidade'))
    print(d1.get('modulo'))
    print(d1.get('telefone', 'a chave telefone não existe'))
"""

"""
d1_keys = d1.keys()
print(d1_keys)

d1_values = d1.values()
print(d1_values)
"""
lista_1 = ["telefone", "casado", "idade"]
lista_2 = ["999-999-999", False, 28]

d2 = {
    lista_1[0]: lista_2[0],
    lista_1[1]: lista_2[1],
    lista_1[2]: lista_2[2]
}

d1.update(d2)

del d1["casado"]
d1.pop("idade")
d1.clear()
print(d1)