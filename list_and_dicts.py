def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Joaquin", "lastname": "Orellana"}

    super_list = [
        {"firstname": "Joaquin", "lastname": "Orellana"},
        {"firstname": "Claudia", "lastname": "Nahuelpan"},
        {"firstname": "Pablo", "lastname": "Retamales"},
        {"firstname": "Carmen", "lastname": "Sotelo"},
        {"firstname": "Fergal", "lastname": "Orellana"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.2]
    }
    # aqui esta pasando las llaves y valores del DICCIONARIO
    for key, value in super_dict.items():
        print(key, " ", value)
        
    # aqui pasamos los DICCIONARIOS de la LISTA y pasamos las llaves y valores de los 
    # DICCIONARIOS anidando las listas con diccionarios
    for i in super_list:
        for key, value in i.items():
            print(key, " ", value)

if __name__ == '__main__':
    run()