
import queryWebsite
import localDatabase
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def client_database():
 todo = [list(i.items()) for i in localDatabase.clientes.get_all()]
 made = render_template('clientes.html', clientes=todo)

 if request.method == 'POST':
  if request.form.get('query'):
   key, val =request.form['query'].split()
   localDatabase.clientes.add_query_field(key, val)
   result = localDatabase.clientes.get_search()
   localDatabase.clientes.delete_queries()
   print(result, localDatabase.clientes.qry, localDatabase.clientes.database.all(), type(key), val)

 return made + str(result)





@app.route("/btn", methods=['GET', 'POST'])
def boton():
 if request.method == 'POST':
  if request.form.get('action1') == 'VALUE1':
   print("boton 1")
  elif request.form.get('action2') == 'VALUE2':
   print("boton 2")
  elif request.form.get('texto'):
   print(request.form['texto'])
  else:
   print("nose")
 elif request.method == 'GET':
  return render_template('botones.html')
 return render_template('botones.html')
