
from tinydb import TinyDB, Query
import queryWebsite
import json

db = TinyDB('clientes.json')
db.truncate()

a = queryWebsite.ApiTalk(queryWebsite.mi_url).get_db()
b = json.loads(a)['data']
for record in b:
 db.insert(record)

class BaseDB():
 def __init__(self, database, fields):
  self.database = database
  self.fields = fields
  self.qry = None

 #PG query
 def add_query_field(self, key, val):
  new_query = (Query()[key] == val)
  if self.qry is None:
   self.qry = new_query
  self.qry = self.qry & new_query

 def delete_queries(self):
  self.qry = None

 def get_search(self):
  return self.database.search(self.qry)

 def get_all(self):
  return self.database.all()

 #PG delete
 def delete(self, cedula):
  self.database.remove(Query()["cedula"] == cedula)

 #PG post
 def post(self, aspirante_json):
  self.database.insert(aspirante_json)


#PG testing

clientes = BaseDB(db, queryWebsite.Aspirante().requerido)
clientes.add_query_field('cedula', '3-761-2397')
