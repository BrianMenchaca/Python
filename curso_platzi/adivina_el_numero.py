import random


def run():
    numero_aleatoria = random.randint(1,100)
    numero_elegido = int(input('Elige un número del 1 al 100:  '))
    while numero_elegido != numero_aleatoria:
        if numero_elegido < numero_aleatoria:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run()