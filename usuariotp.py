from ciudadestp import Ciudades
import base64
from dbatp import dba

class Usuario():
    def __init__(self,id,nombre,apellido,mail,contraseña,fecha_nac,reputacion,ciudades):
        self.id=0
        self.nombre=nombre
        self.apellido=apellido
        self.mail=mail
        self.contraseña=self.encriptar_pass(contraseña)
        self.fecha_nac=fecha_nac
        self.reputacion=reputacion
        self.ciudades=ciudades

    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre 
    def get_apellido(self):
        return self.apellido
    def get_mail(self):
        return self.mail
    def get_contraseña(self):
        return self.contraseña
    def get_fecha_nac(self):
        return self.fecha_nac
    def get_reputacion(self):
        return self.reputacion  
    def get_ciudades(self):
        return self.ciudades
    
    
    def set_id(self,id):
        self.id=id
    def set_nombre(self,nombre):
        self.nombre=nombre
    def set_apellido(self,apellido):
        self.apellido=apellido
    def set_mail(self,mail):
        self.mail=mail
    def set_contraseña(self,contraseña):
        self.contraseña=self.encriptar_pass(contraseña)
    def set_fecha_nac(self,fecha_nac):
        self.fecha_nac=fecha_nac
    def set_reputacion(self,reputacion):
        self.reputacion=reputacion
    def set_ciudades(self,ciudades):
        self.ciudades=ciudades
    
    
    def encriptar_pass(self,contraseña):
        return base64.encodebytes(bytes(contraseña,'utf-8'))
    def desencriptar_pass(self,contraseña):
        return base64.decodebytes(contraseña).decode('UTF-8')

    def save(self):
        sql="insert into usuarios (nombre,apellido,mail,contraseña,fecha_nac,reputacion,id_ciudad) values(%s,%s,%s,%s,%s,%s,%s)"
        val=(self.get_nombre(),self.get_apellido(),self.get_mail(),self.get_contraseña(),self.get_fecha_nac(),self.get_reputacion(),self.get_ciudades())
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
        

    def delete(self,dic):
        sql="delete from usuarios where id=%s"
        val=(self.eliminacionUsuario(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    
    def eliminacionUsuario(self):
        sql="select ID from usuarios where mail = %s and contraseña = %s"
        val=(self.get_mail(),self.get_contraseña())
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchone()
        if result is not None:
            result = result[0]
        return result

    def update(self,dic):
        sql = 'SELECT ID from usuarios WHERE mail = %s'
        val =(self.get_mail(),)
        dba.get_cursor().execute(sql,val)
        result = dba.get_cursor().fetchone()
        self.set_nombre(dic['nombre'])
        self.set_apellido(dic['apellido'])
        self.set_mail(dic['mail'])
        self.set_contraseña(dic['contraseña'])
        self.set_fecha_nac(dic['fecha_nac'])
        self.set_reputacion(dic['reputacion'])
        sql=('update usuarios set nombre=%s,apellido=%s,mail=%s,contraseña=%s,fecha_nac=%s,reputacion=%s,id_ciudad=%s where ID = %s')
        val=(self.get_nombre(),self.get_apellido(),self.get_mail(),self.get_contraseña(),self.get_fecha_nac(),self.get_reputacion(),self.get_ciudades(),result[0])
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()



    


        