from categoriatp import Categorias
from marcastp import Marcas
from dbatp import dba

class Productos():
    def __init__(self,id,nombre,modelo,precio,caracteristicas,calificacion,categorias,marcas):
        self.id=0
        self.nombre=nombre
        self.modelo=modelo
        self.precio=precio
        self.caracteristicas=caracteristicas
        self.calificacion=calificacion
        self.categorias=categorias 
        self.marcas=marcas
        
    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre 
    def get_modelo(self):
        return self.modelo
    def get_precio(self):
        return self.precio
    def get_caracteristicas(self):
        return self.caracteristicas
    def get_calificacion(self):
        return self.calificacion
    def get_categorias(self):
        return self.categorias
    def get_marcas(self):
        return self.marcas
    
    def set_id(self,id):
        self.id=id
    def set_nombre(self,nombre):
        self.nombre=nombre
    def set_modelo(self,modelo):
        self.modelo=modelo
    def set_precio(self,precio):
        self.precio=precio
    def set_caracteristicas(self,caracteristicas):
        self.caracteristicas=caracteristicas
    def set_calificacion(self,calificacion):
        self.calificacion=calificacion
    def set_categorias(self,categorias):
        self.categorias=categorias
    def set_marcas(self,marcas):
        self.marcas=marcas
    
    
    def save(self):
        sql="insert into productos (nombre,modelo,precio,caracteristicas,calificacion,id_categoria,id_marca) values(%s,%s,%s,%s,%s,%s,%s)"
        val=(self.get_nombre(),self.get_modelo(),self.get_precio(),self.get_caracteristicas(),self.get_calificacion(),self.get_categorias(),self.get_marcas())
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

    def delete(self,dic):
        sql="delete from productos where id=%s"
        val=(self.eliminacionProducto(),)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def eliminacionProducto(self):
        sql="select ID from productos where modelo = %s"
        val=(self.get_modelo(),)
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchone()
        if result is not None:
            result = result[0]
        return result

    def update(self,dic):
        sql = 'SELECT ID from productos WHERE modelo = %s'
        val = (self.get_modelo(),)
        dba.get_cursor().execute(sql,val)
        result = dba.get_cursor().fetchone()
        self.set_nombre(dic['nombre'])
        self.set_modelo(dic['modelo'])
        self.set_precio(dic['precio'])
        self.set_caracteristicas(dic['caracteristicas'])
        self.set_calificacion(dic['calificacion'])
        sql = 'UPDATE productos set nombre=%s, modelo=%s, precio=%s, caracteristicas=%s, calificacion=%s, id_categoria=%s, id_marca=%s WHERE ID = %s'
        val = (self.get_nombre(),self.get_modelo(),self.get_precio(),self.get_caracteristicas(),self.get_calificacion(),self.get_categorias(),self.get_marcas(),result[0])
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()


        