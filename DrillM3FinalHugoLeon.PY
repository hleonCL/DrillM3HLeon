nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']
magos = ['Harry Houdini', 'David Blaine', 'Teller']
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = [] #creamos la lista vacia otros
magos_grandiosos = [] #lista de magos grandioso
nombres2 = nombres[:] #clonamos la lista original y asi se trabaja solo en la lista clonada


for nombre in nombres2:
    if nombre in magos:
        magos_grandiosos.append('El gran '+nombre)
    elif nombre in cientificos:
        continue
    else:
        otros.append(nombre)

def imprimir_nombres(nombres2):
    for nombre in nombres2:
        print(nombre)

print('Lista completa de nombres antes de ser modificados:')
imprimir_nombres(nombres)
#le agregamos \n para el salto de linea asi se ve mas ordenado :)
print('\nNombres de los magos grandiosos:')
imprimir_nombres(magos_grandiosos)

print('\nNombres de los científicos:')
imprimir_nombres(cientificos)

print('\nRestantes que no son Magos ni Cientificos:')
imprimir_nombres(otros)