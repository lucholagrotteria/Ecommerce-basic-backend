import mysql.connector

dbconf={
  'host':"localhost",
  'user':"root",
  'password':'',
  'database':'tp'
}

class db():
  def __init__(self):
    self.conexion=mysql.connector.connect(**dbconf)
    self.cursor=self.conexion.cursor()
  def get_cursor(self):
    return self.cursor
  def get_conexion(self):
    return self.conexion

  def listarMarcas(self):
    cursor = self.conexion.cursor()
    cursor.execute('SELECT * FROM marcas ORDER BY nombre ASC')
    result = cursor.fetchall()
    return result

  def listarCategorias(self):
    cursor = self.conexion.cursor()
    cursor.execute('SELECT * FROM categorias ORDER BY nombre ASC')
    result = cursor.fetchall()
    return result

dba=db()
    