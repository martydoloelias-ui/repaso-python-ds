#Tarea 1: Definicion de variables
nombre_producto = "Cortina Roller Blackout"
precio = 25999.90
cantidad_stock = 15
tiene_descuento = True

print(f"Producto: {nombre_producto} | Precio: ${precio}  |  Stock: {cantidad_stock}")

#Tarea 2: Logica de negocio (Bucle + Condicional)
precios = [45.40, 120.00, 99.99, 250.30, 80.00]
precios_de_costo = []
for p in precios:
    precio_costo = p * 0.6 #cuando cuesta hacerlo
    precios_de_costo.append(precio_costo)

for precio_item in precios:
    if precio_item > 100:
         print(f"${precio_item} -> Caro")
    else: 
         print(f"${precio_item} -> Economico")

#Tarea 3: Estructura de Datos Compleja
almacen = {
"Cortina Roller Blackout": 15, 
"Cortina Roller Screen": 8,
"Persiana Americana": 20, 
}
# Agregar un nuevo producto
almacen["Cortina Sunscreen"] = 12
# Consultar stock de un producto
print(f"Stock de Persiana Americana: {almacen['Persiana Americana']}")

#Tarea 4: Modularizacion con funciones
def resumen_estadistico(lista_numeros):
    suma_total = sum(lista_numeros)
    cantidad = len(lista_numeros)
    promedio = suma_total / cantidad
    return {"suma_total": suma_total, "promedio": promedio, "cantidad_elementos": cantidad}

resultado = resumen_estadistico(precios)
print(resultado)

