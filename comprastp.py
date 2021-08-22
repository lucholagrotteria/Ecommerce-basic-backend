from usuariotp import Usuario
from productostp import Productos
from datetime import date
from dbatp import dba

class Compras():
    def __init__(self,id,medio_pago,usuario,productos):
        self.id=0
        self.fecha=date.today()
        self.medio_pago=medio_pago
        self.usuario=usuario
        self.productos=productos

    def get_id(self):
        return self.id
    def get_importe(self):
        return self.importe
    def get_fecha(self):
        return self.fecha
    def get_medio_pago(self):
        return self.medio_pago 
    def get_usuario(self):
        return self.usuario 
    def get_productos(self):
        return self.productos 

    def set_id(self,id):
        self.id=id
    def set_importe(self,importe):
        self.importe=importe
    def set_fecha(self,fecha):
        self.fecha=fecha
    def set_medio_pago(self,medio_pago):
        self.medio_pago=medio_pago
    def set_usuario(self,usuario):
        self.usuario=usuario
    def set_productos(self,productos):
        self.productos=productos    

    def save(self):
        sql="insert into compras (medio_pago,fecha,id_usuario,id_producto) values(%s,%s,%s,%s)"
        val=(self.get_medio_pago(),self.get_fecha(),self.get_usuario(),self.get_productos())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

    def delete(self):
        sql="delete from compras where id=%s"
        val=(self.get_id(),)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
    


    