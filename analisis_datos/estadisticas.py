# estadisticas.py
def media(datos):
    """ Esta función calcula la media aritmética de una lista con valores numéricos

    Args:
        datos (lista): Lista de números

    Returns:
        float: flotante de la media aritmética estadística
    """
    return sum(datos) / len(datos)

def calcular_mediana(datos):
    datos_sorted = sorted(datos)
    n = len(datos)
    mid = n // 2
    if n % 2 == 0:
        return (datos_sorted[mid - 1] + datos_sorted[mid]) / 2.0
    else:
        return datos_sorted[mid]

