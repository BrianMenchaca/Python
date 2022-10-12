def run():
    mi_diccionario = {
        'k1': 100,
        'k2': 200,
        'k3': 300,
    }
    for llave,valor in mi_diccionario.items():
        print(llave + ': ' + str(valor))


if __name__ == '__main__':
    run()