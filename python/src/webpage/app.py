
import queryWebsite
import localDatabase
from flask import Flask, render_template, request

app = Flask(__name__)

def to_list(dlist):
 if dlist:
  return [sorted(dlist[0].keys()), [sorted(i.items()) for i in dlist]]
 return []

@app.route("/", methods=['GET', 'POST', 'DELETE'])
def client_database():

 result = []
 aspi = queryWebsite.Aspirante()

 if request.method == 'POST':
  if request.form['query'] == 'search':
   key, val = request.form['key'], request.form['val']
   localDatabase.clientes.add_query_field(key, val)
   result = localDatabase.clientes.get_search()
   #if type(result) is dict:
    #result = [result]
   localDatabase.clientes.delete_queries()
  #fields in a form get identified by their name, not their id.
  if request.form['query'] == 'submit':
   new_aspirant = {k:v for k,v in zip(aspi.requerido, request.form.getlist('fields[]'))}
   print(new_aspirant)
   localDatabase.clientes.post(queryWebsite.Aspirante(new_aspirant).get_post())
 if request.method == 'DELETE':
  if request.form['query'] == 'delete':
   print("\t borrar")
   ceda = request.form['borrar']
   localDatabase.clientes.delete(ceda)
  
 made = render_template('clientes.html', clientes=to_list(localDatabase.clientes.get_all()), seleccion=to_list(result), aspirantefields=aspi.requerido)
 return made

