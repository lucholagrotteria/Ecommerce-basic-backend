def listarMarcas(marcas):
    print('\nMarcas: \n')
    contador = 1
    for i in marcas:
        print('--------------------------------------------------------------')
        datos = '{0}. - Nombre: {1}'
        print(datos.format(contador,i[1]))
        contador += 1
    print('--------------------------------------------------------------')
    print(' ')

def listarCategorias(categorias):
    print('\nCategorias: \n')
    contador = 1
    for i in categorias:
        print('---------------------------------------------------------------')
        datos = '{0}. Nombre: {1}'
        print(datos.format(contador,i[1]))
        contador +=1
    print('--------------------------------------------------------------')    
    print(' ') 

