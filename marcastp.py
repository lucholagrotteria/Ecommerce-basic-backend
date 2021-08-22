from categoriatp import Categorias 
from dbatp import dba

class Marcas():
    def __init__(self,id,nombre,categorias):
        self.id=0
        self.nombre=nombre
        self.categorias=categorias

    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre
    def get_categorias(self):
        return self.categorias 

    def set_id(self,id):
        self.id=id
    def set_nombre(self,nombre):
        self.nombre=nombre
    def set_categorias(self,categorias):
        self.categorias=categorias
    
    def save(self):
        sql="insert into usuario (nombre,categorias) values(%s,%s)"
        val=(self.get_nombre(),self.get_categorias())
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

    def delete(self):
        sql="delete from usuario where id=%s"
        val=(self.get_id(),)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
