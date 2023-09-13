def complex_delete(a_dictionary, value):
    to_delete = list()
    for k, v in a_dictionary.items():
        if v == value:
            to_delete.append(k)
    for k in to_delete:
        del a_dictionary[k]
