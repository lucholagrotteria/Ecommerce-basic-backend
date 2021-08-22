from dbatp import dba

class Ciudades():
    def __init__(self,id,nombre):
        self.id=0
        self.nombre=nombre

    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre 
    
    def set_id(self,id):
        self.id=id
    def set_nombre(self,nombre):
        self.nombre=nombre

    def save(self):
        sql="insert into ciudades (nombre) values(%s)"
        val=(self.get_nombre(),)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

    def delete(self):
        sql="delete from ciudades where id=%s"
        val=(self.get_id(),)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

