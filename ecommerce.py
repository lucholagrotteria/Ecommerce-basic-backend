from usuariotp import Usuario
from productostp import Productos
from comprastp import Compras
from ciudadestp import Ciudades
from validaciontp import validator
from categoriatp import Categorias
from marcastp import Marcas
from dbatp import db
import listadostp
import getpass 

def Inicio():
    continuar = True 
    while(continuar):
        opcionCorrecta = False 
        print('\n                      INICIO                     \n')
        while(not opcionCorrecta):
            print('\n***************************************************\n')
            print('1.Administrador')
            print('2.Cliente')
            print('3.Salir')
            print('\n***************************************************\n')
            opcionInicio = input('Ingrese una opcion: ')
            if opcionInicio < '1' or opcionInicio > '3':
                print('\nOpcion incorrecta. Intente nuevamente\n') 
            elif opcionInicio == '3':
                continuar = False
                print('\nGracias por visitar EROCK!\n')
                break
            else:
                opcionCorrecta = True
                ejecutarInicio(opcionInicio)

def ejecutarInicio(opcionInicio):
    if opcionInicio == '1':
        return Configuracion()
    if opcionInicio == '2':
        return menuInicio()

def Configuracion():
    continuar = True 
    while(continuar):
        opcionCorrecta = False
        print('\n                   CONFIGURACION                 \n')
        while(not opcionCorrecta):
            print('\n***************************************************\n')
            print('1.Registro Producto')
            print('2.Eliminar Producto')
            print('3.Modificar Producto')
            print('4.Salir')
            print('\n***************************************************\n')
            opcionConfiguracion = input('Ingrese una opcion: ')
            if opcionConfiguracion < '1' or opcionConfiguracion > '4':
                print('\nOpcion incorrecta. Intente nuevamente\n') 
            elif opcionConfiguracion == '4':
                continuar = False
                print('\nGracias por visitar EROCK\n')
                break
            else:
                opcionCorrecta = True
                ejecutarConfiguracion(opcionConfiguracion)

def ejecutarConfiguracion(opcionConfiguracion):
    listcategorias = []
    listmarcas = []
    if opcionConfiguracion == '1':
        print('\n                REGISTRO DE PRODUCTO                \n')
        print('\n***************************************************\n')
        formproducto={}
        formproducto['nombre'] = input('Nombre: ')
        formproducto['modelo'] = input('Modelo: ')
        formproducto['precio'] = input('Precio: ')
        formproducto['caracteristicas'] = input('Caracteristicas: ')
        formproducto['calificacion'] = input('Calificacion: ')
        formproducto['id_categoria'] = input('Categoria: ')
        formproducto['id_marca'] = input('Marca: ')
        if validator.validar_productos(formproducto) == {}:
            if len(formproducto['id_categoria']) > 1:
                dba = db()
                sql='SELECT nombre FROM categorias'
                dba.get_cursor().execute(sql)
                result=dba.get_cursor().fetchall()
                for i in result:
                    listcategorias.append(i[0])
                if (formproducto['id_categoria'] in listcategorias) == True:
                    sql='SELECT ID FROM categorias WHERE nombre = %s'
                    val=(formproducto['id_categoria'],)
                    dba.get_cursor().execute(sql,val)
                    result=dba.get_cursor().fetchone()
                    categoria1=Categorias(0,formproducto['id_categoria'])
                    categoria1.set_id(result[0])
                else:
                    categoria1=Categorias(0,formproducto['id_categoria'])
                    sql='INSERT INTO categorias (nombre) VALUES(%s)'
                    val=((formproducto['id_categoria']),)
                    dba.get_cursor().execute(sql,val)
                    dba.get_conexion().commit()
                    categoria1.set_id(dba.get_cursor().lastrowid)
            if len(formproducto['id_marca']) > 1:
                dba = db()
                sql='SELECT nombre FROM marcas'
                dba.get_cursor().execute(sql)
                result=dba.get_cursor().fetchall()
                for j in result:
                    listmarcas.append(j[0])
                if (formproducto['id_marca'] in listmarcas) == True:
                    sql='SELECT ID FROM marcas WHERE nombre = %s'
                    val=(formproducto['id_marca'],)
                    dba.get_cursor().execute(sql,val)
                    result=dba.get_cursor().fetchone()
                    marca1=Marcas(0,formproducto['id_marca'],categoria1)
                    marca1.set_id(result[0])
                else:
                    marca1=Marcas(0,formproducto['id_marca'],categoria1)
                    sql='INSERT INTO marcas (nombre) VALUES(%s)'
                    val=((formproducto['id_marca']),)
                    dba.get_cursor().execute(sql,val)
                    dba.get_conexion().commit()
                    marca1.set_id(dba.get_cursor().lastrowid)
            producto1 = Productos(0,formproducto['nombre'],formproducto['modelo'],formproducto['precio'],formproducto['caracteristicas'],formproducto['calificacion'],categoria1.get_id(),marca1.get_id())
            producto1.save()
            print('\nProducto registrado exitosamente\n')
        else:
            print(validator.validar_productos(formproducto))
    
    if opcionConfiguracion == '2':
        print('\n               ELIMINACION DE PRODUCTO               \n')
        print('\n***************************************************\n')
        formdeleteproducto = {}
        formdeleteproducto['modelo'] = input('Modelo: ')
        if validator.deleteProducto(formdeleteproducto) == {}:
            producto1 = Productos(0,'',formdeleteproducto['modelo'],'','','','','')
            producto1.delete(formdeleteproducto)
            print('\nProducto eliminado exitosamente.\n')
        else:
            print(validator.deleteProducto(formdeleteproducto))

    if opcionConfiguracion == '3':
        print('\n               MODIFICACION DE PRODUCTO               \n')
        print('\n***************************************************\n')
        formproductomodif={}
        formproductomodif['nombre'] = input('Nombre: ')
        formproductomodif['modelo'] = input('Modelo: ')
        formproductomodif['precio'] = input('Precio: ')
        formproductomodif['caracteristicas'] = input('Caracteristicas: ')
        formproductomodif['calificacion'] = input('Calificacion: ')
        formproductomodif['id_categoria'] = input('Categoria: ')
        formproductomodif['id_marca'] = input('Marca: ')
        if validator.productos_update(formproductomodif) == {}:
            if len(formproductomodif['id_categoria']) > 1:
                dba = db()
                sql='SELECT nombre FROM categorias'
                dba.get_cursor().execute(sql)
                result=dba.get_cursor().fetchall()
                for i in result:
                    listcategorias.append(i[0])
                if (formproductomodif['id_categoria'] in listcategorias) == True:
                    sql='SELECT ID FROM categorias WHERE nombre = %s'
                    val=(formproductomodif['id_categoria'],)
                    dba.get_cursor().execute(sql,val)
                    result=dba.get_cursor().fetchone()
                    categoria1=Categorias(0,formproductomodif['id_categoria'])
                    categoria1.set_id(result[0])
                else:
                    categoria1=Categorias(0,formproductomodif['id_categoria'])
                    sql='INSERT INTO categorias (nombre) VALUES(%s)'
                    val=((formproductomodif['id_categoria']),)
                    dba.get_cursor().execute(sql,val)
                    dba.get_conexion().commit()
                    categoria1.set_id(dba.get_cursor().lastrowid)
            if len(formproductomodif['id_marca']) > 1:
                dba = db()
                sql='SELECT nombre FROM marcas'
                dba.get_cursor().execute(sql)
                result=dba.get_cursor().fetchall()
                for j in result:
                    listmarcas.append(j[0])
                if (formproductomodif['id_marca'] in listmarcas) == True:
                    sql='SELECT ID FROM marcas WHERE nombre = %s'
                    val=(formproductomodif['id_marca'],)
                    dba.get_cursor().execute(sql,val)
                    result=dba.get_cursor().fetchone()
                    marca1=Marcas(0,formproductomodif['id_marca'],categoria1)
                    marca1.set_id(result[0])
                else:
                    marca1=Marcas(0,formproductomodif['id_marca'],categoria1)
                    sql='INSERT INTO marcas (nombre) VALUES(%s)'
                    val=((formproductomodif['id_marca']),)
                    dba.get_cursor().execute(sql,val)
                    dba.get_conexion().commit()
                    marca1.set_id(dba.get_cursor().lastrowid)
            producto1 = Productos(0,formproductomodif['nombre'],formproductomodif['modelo'],formproductomodif['precio'],formproductomodif['caracteristicas'],formproductomodif['calificacion'],categoria1.get_id(),marca1.get_id())
            print(producto1.get_modelo())
            producto1.set_marcas(marca1.get_id())
            producto1.set_categorias(categoria1.get_id())
            producto1.update(formproductomodif)
            print('\nProducto modificado exitosamente.\n')
        else:
            print(validator.productos_update(formproductomodif))
   
def menuInicio():
    continuar = True 
    while(continuar):
        opcionCorrecta = False 
        print('\n                BIENVENIDOS A EROCK                   \n')
        while(not opcionCorrecta):
            print('\n***************************************************\n')
            print('1.Iniciar Sesion')
            print('2.Registrarse')
            print('3.Salir')
            print('\n***************************************************\n')
            opcionMenu = input('Ingrese una opcion: ')
            if opcionMenu < '1' or opcionMenu > '3':
                print('\nOpcion incorrecta. Intente nuevamente.\n') 
            elif opcionMenu == '3':
                continuar = False
                print('\nGracias por visitar EROCK\n')
                break
            else:
                opcionCorrecta = True
                ejecutarMenuInicio(opcionMenu)

def ejecutarMenuInicio(opcionMenu):
    if opcionMenu == '1':
        print('\n                       LOGIN                       \n')
        print('\n***************************************************\n')
        return validar_login()
    elif opcionMenu == '2':
        print('\n                     REGISTRO                       \n')
        print('\n***************************************************\n')
        return validar_usuario()

def validar_login():
    dba = db()
    formlogin = {}
    formlogin['mail'] = input('Mail: ')
    formlogin['contraseña'] = getpass.getpass('Contraseña: ')
    if validator.validar_login(formlogin) is not False:
        user1 = Usuario(*validator.validar_login(formlogin))
        sql = 'SELECT ID from usuarios where mail = %s'
        val = ((formlogin['mail']),)
        dba.get_cursor().execute(sql,val)
        result = dba.get_cursor().fetchone()
        user1.set_id(result[0])
        print('Sesion iniciada. Bienvenido/a', user1.get_nombre(),user1.get_apellido())
        Ajustes(user1)
    else:
        print('\nUsuario o contraseña incorrecta.\n')


listciu = []
def validar_usuario():
    formuser={}
    formuser['nombre'] = input('Nombre: ')
    formuser['apellido'] = input('Apellido: ')
    formuser['mail'] = input('Mail: ')
    formuser['contraseña'] = input('Contraseña: ')
    formuser['ccontraseña'] = input('Confirme la contraseña: ')
    formuser['fecha_nac'] = input('Fecha de nacimiento: ')
    formuser['reputacion'] = input('Reputacion: ')
    formuser['id_ciudad'] = input('Ciudad: ') 
    if validator.validar_usuario(formuser) == {}:
        if len(formuser['id_ciudad']) > 1:
            dba = db()
            sql='SELECT nombre FROM ciudades'
            dba.get_cursor().execute(sql)
            result=dba.get_cursor().fetchall()
            for i in result:
                listciu.append(i[0])
            if (formuser['id_ciudad'] in listciu) == True:
                sql='SELECT ID FROM ciudades WHERE nombre = %s'
                val=(formuser['id_ciudad'],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                ciudad1=Ciudades(0,formuser['id_ciudad'])
                ciudad1.set_id(result[0])
            else:
                ciudad1=Ciudades(0,formuser['id_ciudad'])
                sql='INSERT INTO ciudades (nombre) VALUES(%s)'
                val=((formuser['id_ciudad']),)
                dba.get_cursor().execute(sql,val)
                dba.get_conexion().commit()
                ciudad1.set_id(dba.get_cursor().lastrowid)
        user1=Usuario(0,formuser['nombre'],formuser['apellido'],formuser['mail'],formuser['contraseña'],formuser['fecha_nac'],formuser['reputacion'],formuser['id_ciudad'])
        user1.set_ciudades(ciudad1.get_id())
        user1.save()
        print('\nUsuario registrado exitosamente.\n')
        Ajustes(user1)
    else:
        print(validator.validar_usuario(formuser))

def Ajustes(user1):
    continuar = True 
    while(continuar):
        opcionCorrecta = False 
        while(not opcionCorrecta):
            print('\n                     AJUSTES               \n')
            print('\n***************************************************\n')
            print('1.Eliminar Usuario')
            print('2.Modificar Usuario')
            print('3.Menú de Productos')
            print('\n***************************************************\n')
            opcionAjustes = input('Ingrese una opcion: ')
            if opcionAjustes < '1' or opcionAjustes > '3':
                print('\nOpcion incorrecta. Intente nuevamente.\n')
            if opcionAjustes == '3':
                continuar = False 
                print('\nSaliste del menu de ajustes.\n')
                menuProductos(user1)
                break
            else:
                opcionCorrecta = True 
                ejecutarAjustes(opcionAjustes,user1)

def ejecutarAjustes(opcionAjustes,user1):
    if opcionAjustes == '1':
        print('\n                ELIMINACION DE USUARIO               \n')
        print('\n***************************************************\n')
        formdelete = {}
        formdelete['mail'] = input('Mail: ')
        formdelete['contraseña'] = input('Contraseña: ')
        if validator.eliminarUsuario(formdelete) == {}:
            user1=Usuario(0,'','',formdelete['mail'],formdelete['contraseña'],'','','')
            user1.delete(formdelete)
            print('\nUsuario eliminado exitosamente.\n')
        else:
            print(validator.eliminarUsuario(formdelete))

    if opcionAjustes == '2':
        print('\n               MODIFICACION DE USUARIO             \n')
        print('\n***************************************************\n')
        formmodif={}
        formmodif['nombre'] = input('Nombre: ')
        formmodif['apellido'] = input('Apellido: ')
        formmodif['mail'] = input('Mail: ')
        formmodif['contraseña'] = input('Contraseña: ')
        formmodif['ccontraseña'] = input('Confirme la contraseña: ')
        formmodif['fecha_nac'] = input('Fecha de nacimiento: ')
        formmodif['reputacion'] = input('Reputacion: ')
        formmodif['id_ciudad'] = input('Ciudad: ') 
        if validator.validar_usuario_update(formmodif) == {}:
            if len(formmodif['id_ciudad']) > 1:
                dba = db()
                sql='SELECT nombre FROM ciudades'
                dba.get_cursor().execute(sql)
                result=dba.get_cursor().fetchall()
                for i in result:
                    listciu.append(i[0])
                if (formmodif['id_ciudad'] in listciu) == True:
                    sql='SELECT ID FROM ciudades WHERE nombre = %s'
                    val=(formmodif['id_ciudad'],)
                    dba.get_cursor().execute(sql,val)
                    result=dba.get_cursor().fetchone()
                    ciudad1=Ciudades(0,formmodif['id_ciudad'])
                    ciudad1.set_id(result[0])
                else:
                    ciudad1=Ciudades(0,formmodif['id_ciudad'])
                    sql='INSERT INTO ciudades (nombre) VALUES(%s)'
                    val=((formmodif['id_ciudad']),)
                    dba.get_cursor().execute(sql,val)
                    dba.get_conexion().commit()
                    ciudad1.set_id(dba.get_cursor().lastrowid)
            user1 = Usuario(0,formmodif['nombre'],formmodif['apellido'],formmodif['mail'],formmodif['contraseña'],formmodif['fecha_nac'],formmodif['reputacion'],ciudad1.get_id())
            print(ciudad1.get_id())
            user1.set_ciudades(ciudad1.get_id())
            print(ciudad1.get_id())
            user1.update(formmodif)
            print('\nUsuario modificado exitosamente.\n')
        else: 
            print(validator.validar_usuario_update(formmodif))

def menuProductos(user1):
    continuar = True 
    while(continuar):
        opcionCorrecta = False 
        while(not opcionCorrecta):
            print('\n                     PRODUCTOS                       \n')
            print('\n***************************************************\n')
            print('1.Productos')
            print('2.Marcas')
            print('3.Categorias')
            print('4.Salir')
            print('\n***************************************************\n')
            opcion = input('Inserte una opcion: ')
            if opcion < '1' or opcion > '4':
                print('\nOpcion incorrecta. Intente nuevamente\n.') 
            elif opcion == '4':
                continuar = False
                break
            else:
                opcionCorrecta = True
                ejecutarMenuProducto(opcion,user1)

def ejecutarMenuProducto(opcion,user1):
    dba = db()
    if opcion == '1':
        Carrito(user1)
    if opcion == '2':
        marcas = dba.listarMarcas()
        listadostp.listarMarcas(marcas)
    if opcion == '3':
        categorias = dba.listarCategorias()
        listadostp.listarCategorias(categorias)

def Carrito(user1):
    dba = db()
    sql = 'SELECT * FROM productos'
    dba.get_cursor().execute(sql)
    result = dba.get_cursor().fetchall()
    for i in result:
        print('\n--------------------------------------------------------------\n')
        datos = 'Codigo: {0} - Nombre: {1} - Modelo: {2} - Precio: {3} - Marca: {4}'
        print(datos.format(i[0],i[1],i[2],i[3],i[7]))
    print('\n--------------------------------------------------------------\n')
    codigo = int(input('Ingrese el codigo del producto que desea comprar: '))
    if codigo > 39 and codigo < 55:
        finalizarCompra(codigo,user1)
    else:
        print('\nOpcion incorrecta.\n')

listaCompra = []
def finalizarCompra(codigo,user1):
    dba = db()
    sql = 'SELECT ID,nombre,precio FROM productos WHERE ID = %s'
    val = ((codigo),)
    dba.get_cursor().execute(sql,val)
    result = dba.get_cursor().fetchone()
    for i in result:
        listaCompra.append(i)
    datos = 'Codigo: {} - Nombre: {} - Precio: {}'
    print(datos.format(result[0],result[1],result[2]))
    print(listaCompra)
    comp1=Compras(0,'tarjeta',user1.get_id(),result[0])
    comp1.set_usuario(user1.get_id())
    comp1.set_productos(result[0])
    comp1.save()
    print('\nCompra exitosa.\n')
    menuFinalizacion(user1)
    

def menuFinalizacion(user1):
    continuar = True 
    while(continuar):
        opcionCorrecta = False 
        while(not opcionCorrecta):
            print('\n*********************************************************\n')
            print('1.Continuar comprando')
            print('2.Detalle de compra')
            print('3.Salir')
            print('\n*********************************************************\n')
            opcion = input('Inserte una opcion: ')
            if opcion < '1' or opcion > '3':
                print('\nOpcion incorrecta. Intente nuevamente.\n') 
            elif opcion == '3':
                continuar = False
                break
            else:
                opcionCorrecta = True
                ejecutarFinalizacion(opcion,user1)

def ejecutarFinalizacion(opcion,user1):
    if opcion == '1':
        return menuProductos(user1)
    else:
        print('\nOpcion incorrecta.\n')
    
    



Inicio()