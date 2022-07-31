
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
  self.requerido = "nacionalidad status apellido cedula sexo id nombre id_aspirante edad fecha_nacimiento".split()
  self.data = {}

  if fields is None:
   fields = {k:None for k in self.requerido}

  for key in self.requerido:
   try:
    self.data[key] = fields[key]
   except KeyError:
    self.data[key] = None

 def set_field(self, key, val):
  self.data[key] = val

 def get_field(self, key):
  return self.data[key]

 def validate(self):
  return (all(self.data.values()), [k for k,v in self.data.items() if v is None])

 def undefined(self):
  retn = []
  for key in self.requerido:
   val = self.data[key]
   if val is None:
    retn.append(key)
  return retn

 def render(self):
  return json.dumps(self.data)
    
class ApiTalk():

 def __init__(self, url):
  self.url = url
  self.db = UrlQuery(url)

 #PG get requests

 def run_request(self, url_api):
  with urllib.request.urlopen(url_api) as db:
   json_base = db.read()
  return json_base

 def query_add(self, key, val):
  return self.db.query_field(key, val)

 def clean_request(self):
  self.db.reset_query()

 def get_db(self):
  return self.run_request(self.url)

 #PG post requests

 #TODO fails with internal server error.
 def _post_aspirante(self, aspirante):
  data = aspirante.render().encode('utf-8')
  reqt = urllib.request.Request(self.url, data=data)

  with urllib.request.urlopen(reqt) as response:
   return response.read()

#PG pruebas

mi_url = "http://3.138.208.231:9041/api/advisers/cliente/"
aspe = Aspirante()
aspe.set_field("status", 3)
aspe.set_field("cedula", "8-888-8888")
aspe.set_field("nombre", "Ruben")
aspe.set_field("apellido", "Blades")
aspe.set_field("id_aspirante", 10)
#aspe.set_field("id", 20)
aspe.set_field("edad", '80')
aspe.set_field("fecha_nacimiento", '1970-01-01')
aspe.set_field("sexo", "masculino")
aspe.set_field("nacionalidad", "panameno")


#PG cruft
#database_url = UrlQuery(mi_url)
#database_url.query_field("cedula", "3-761-2498")
#
#def request_db(dburl):
 #with urllib.request.urlopen(dburl) as db:
  #json_base = db.read()
 #return json_base
#
#json_loaded = json.loads(request_db(database_url.render()))
#database_url.reset_query()
#other = json.loads(request_db(database_url.render()))
#
#print(json_loaded, other, sep="\n")

#try:
 #print(ApiTalk(mi_url).post_aspirante(aspe))
#except BaseException as err:
 #print(err.args, err.code, err.fp, err.geturl, err.hdrs, err.headers, err.info, err.msg, err.name, err.reason, err.status, sep="\n")
