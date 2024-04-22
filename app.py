import random

def tirar_dado():
    return random.randint(1, 6)

def calcular_puntaje(dado1, dado2):
    if dado1 == 4 and dado2 != 4:
        return dado2
    elif dado1 != 4 and dado2 == 4:
        return dado1
    else:
        return 0

def jugar():
    # Juan tira los dados
    dado1_juan, dado2_juan = tirar_dado(), tirar_dado()
    puntaje_juan = calcular_puntaje(dado1_juan, dado2_juan)

    # Juan decide si tira nuevamente uno de los dados
    if puntaje_juan == 0: #Si el puntaje es 0, tira ambos dados nuevamente
        dado_1_juan, dado2_juan = tirar_dado(), tirar_dado()
        puntaje_juan = calcular_puntaje(dado1_juan, dado2_juan)
    elif puntaje_juan <= 3: #Si el puntaje es menor a 3, tira el dado que no es 4
        puntaje_juan = tirar_dado()

    # María tira los dados
    dado1_maria, dado2_maria = tirar_dado(), tirar_dado()
    puntaje_maria = calcular_puntaje(dado1_maria, dado2_maria)
    
    #Si maría saca 0
    if puntaje_maria == 0:
        dado1_maria, dado2_maria = tirar_dado(), tirar_dado()
        puntaje_maria = calcular_puntaje(dado1_maria, dado2_maria)
    # María decide si tira nuevamente uno de los dados
    elif puntaje_maria < puntaje_juan: #Si el puntaje de maria es menor a juan
        puntaje_maria = tirar_dado()

    # Determinar el resultado de la partida
    if puntaje_juan > puntaje_maria:
        return "Juan"
    elif puntaje_maria > puntaje_juan:
        return "María"
    else:
        return "Empate"


# Simular el juego n veces
valores_n = [1000, 10000, 100000]  # Valores de n que deseas probar

for n in valores_n:
    resultados = {"Juan": 0, "María": 0, "Empate": 0}
    for _ in range(n):
        resultado = jugar()
        resultados[resultado] += 1

    # Calcular frecuencias relativas
    frec_relativa_juan = resultados["Juan"] / n
    frec_relativa_maria = resultados["María"] / n
    frec_relativa_empate = resultados["Empate"] / n

    print(f"Simulación n = {n}")
    print(f"Frecuencia relativa de Juan ganando: {frec_relativa_juan}")
    print(f"Frecuencia relativa de María ganando: {frec_relativa_maria}")
    print(f"Frecuencia relativa de Empate: {frec_relativa_empate}")
    print("\n")
