from validate_email import validate_email
from dbatp import dba
import base64 

class Validator():
    def __init__(self):
        pass 

    def validar_usuario(self,dic):
        datosFinales={}
        errores={}
        SpecialSym =['$', '@', '#', '%']
        for x,y in dic.items():
            datosFinales[x]=y.strip()
        
        if datosFinales['nombre']=='':
            errores['nombre']='Campo nombre vacio'
        if datosFinales['apellido']=='':
            errores['apellido']='Campo apellido vacio'
        if datosFinales['mail']=='':
            errores['mail']='Campo mail vacio'
        if datosFinales['contraseña']=='':
            errores['contraseña']='Campo contraseña vacio'
        if datosFinales['fecha_nac']=='':
            errores['fecha_nac']='Campo fecha_nac vacio'
        if datosFinales['reputacion']=='':
            errores['reputacion']='Campo reputacion vacio'
        if datosFinales['id_ciudad']=='':
            errores['id_ciudad']='Campo id_ciudad vacio'

        if len(datosFinales['contraseña']) < 6:
            errores['contraseña']='La contraseña debe contener mas de 6 caracteres'
        elif not any(char.isdigit() for char in datosFinales['contraseña']):
            errores['contraseña']='La contraseña debe contener un caracter numeral'
        elif not any(char in SpecialSym for char in datosFinales['contraseña']):
            errores['contraseña']='La contraseña debe contener al menos un caracter especial $@#'

        if datosFinales['ccontraseña'] =='':
            errores['ccontraseña'] = 'Introduzca la confirmacion de la contraseña'
        elif datosFinales['ccontraseña'] != datosFinales['ccontraseña']:
            errores['ccontraseña'] = 'Las contraseñas ingresadas no coinciden'
       
        if datosFinales["mail"]=="":
            errores["mail"] = "Hubo error en el mail porque esta vacio"
        elif validate_email(datosFinales["mail"])==False:
            errores["mail"] = "El mail no es un mail"
        
        if errores=={}:
            sql='select ID from usuarios where mail=%s'
            val=(datosFinales['mail'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['mail']='El mail ya esta registrado en nuestra base'
                return errores
        return errores

    def validar_usuario_update(self,dic):
        datosFinales={}
        errores={}
        SpecialSym =['$', '@', '#', '%']
        for x,y in dic.items():
            datosFinales[x]=y.strip()
        
        if datosFinales['nombre']=='':
            errores['nombre']='Campo nombre vacio'
        if datosFinales['apellido']=='':
            errores['apellido']='Campo apellido vacio'
        if datosFinales['mail']=='':
            errores['mail']='Campo mail vacio'
        if datosFinales['contraseña']=='':
            errores['contraseña']='Campo contraseña vacio'
        if datosFinales['fecha_nac']=='':
            errores['fecha_nac']='Campo fecha_nac vacio'
        if datosFinales['reputacion']=='':
            errores['reputacion']='Campo reputacion vacio'
        if datosFinales['id_ciudad']=='':
            errores['id_ciudad']='Campo id_ciudad vacio'

        if len(datosFinales['contraseña']) < 6:
            errores['contraseña']='La contraseña debe contener mas de 6 caracteres'
        elif not any(char.isdigit() for char in datosFinales['contraseña']):
            errores['contraseña']='La contraseña debe contener un caracter numeral'
        elif not any(char in SpecialSym for char in datosFinales['contraseña']):
            errores['contraseña']='La contraseña debe contener al menos un caracter especial $@#'

        if datosFinales['ccontraseña'] =='':
            errores['ccontraseña'] = 'Introduzca la confirmacion de la contraseña'
        elif datosFinales['ccontraseña'] != datosFinales['ccontraseña']:
            errores['ccontraseña'] = 'Las contraseñas ingresadas no coinciden'
       
        if datosFinales["mail"]=="":
            errores["mail"] = "Hubo error en el mail porque esta vacio"
        elif validate_email(datosFinales["mail"])==False:
            errores["mail"] = "El mail no es un mail"
        if errores=={}:
            return errores
        return errores

    def eliminarUsuario(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()
        if datosFinales['mail']=='':
            errores['mail']='Campo mail vacio'
        if datosFinales['contraseña']=='':
            errores['contraseña']='Campo contraseña vacio'
        return errores
        

    def validar_login(self,dic):
        sql='select * from usuarios where mail=%s'
        val=(dic['mail'],)
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchall()
        if result == []:
            return False 
        if base64.decodebytes(bytes(result[0][4].strip(),'utf-8')).decode('UTF-8')==dic['contraseña']:
            return result[0]
        else:
            return False
    
    def validar_productos(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()
        
        if datosFinales['nombre']=='':
            errores['nombre']='Campo nombre vacio'
        if datosFinales['modelo']=='':
            errores['modelo']='Campo modelo vacio'
        if datosFinales['precio']=='':
            errores['precio']='Campo precio vacio'
        if datosFinales['caracteristicas']=='':
            errores['caracteristicas']='Campo caracteristicas vacio'
        if datosFinales['calificacion']=='':
            errores['calificacion']='Campo calificacion vacio'
        if datosFinales['id_categoria']=='':
            errores['id_categoria']='Campo categoria vacio'
        if datosFinales['id_marca']=='':
            errores['id_marca']='Campo marca vacio'
        return errores

    def productos_update(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()
        
        if datosFinales['nombre']=='':
            errores['nombre']='Campo nombre vacio'
        if datosFinales['modelo']=='':
            errores['modelo']='Campo modelo vacio'
        if datosFinales['precio']=='':
            errores['precio']='Campo precio vacio'
        if datosFinales['caracteristicas']=='':
            errores['caracteristicas']='Campo caracteristicas vacio'
        if datosFinales['calificacion']=='':
            errores['calificacion']='Campo calificacion vacio'
        if datosFinales['id_categoria']=='':
            errores['id_categoria']='Campo categoria vacio'
        if datosFinales['id_marca']=='':
            errores['id_marca']='Campo marca vacio'
        if errores=={}:
            return errores
        return errores

    def deleteProducto(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()
        if datosFinales['modelo']=='':
            errores['modelo']='Campo modelo vacio'
        return errores


validator = Validator()
        


    

