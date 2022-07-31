
import urllib.request
import json

class UrlQuery():
 def __init__(self, url):
  self.url = url
  self.query_parameters = []

 def query_field(self, key, val):
  retn = f"{key}={val}"
  self.query_parameters.append(retn)
  return self

 def reset_query(self):
  self.query_parameters = []
  return self

 def render(self):
  query = "?" + "&".join(self.query_parameters)
  return self.url + query


class Aspirante():
 def __init__(self, fields=None):
  self.requerido = "status apellido cedula sexo id nombre id_aspirante edad fecha_nacimiento".split()
  if fields is None:
   self.data = {k:None for k in self.requerido}

 def set_field(self, key, val):
  self.data[key] = val

 def get_field(self, key):
  return self.data[key]

 def validate(self):
  return self.requerido == list(self.data.keys())

 def undefined(self):
  retn = []
  for key in self.requerido:
   try:
    val = self.data[key]
    if val is None:
     retn.append(key)
   except KeyError:
    retn.append(key)
  return retn
    

database_url = UrlQuery("http://3.138.208.231:9041/api/advisers/cliente/")
database_url.query_field("cedula", "3-761-2498")

def request_db(dburl):
 with urllib.request.urlopen(dburl) as db:
  json_base = db.read()
 return json_base

json_loaded = json.loads(request_db(database_url.render()))
database_url.reset_query()
other = json.loads(request_db(database_url.render()))

print(json_loaded, other, sep="\n")