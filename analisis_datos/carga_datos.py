import random

def generar_lista_de_compras():
    productos = {
        'manzanas': 1000,
        'bananos': 150,
        'cerezas': 2000,
        'naranjas': 900,
        'pan': 2275,
        'leche': 900,
        'huevos': 3400,
        'queso': 4500        
    }
    seleccion = random.sample(list(productos.items()),5) # Selecciona 5 productos de la lista
    return seleccion