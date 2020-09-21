from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return '''
  <h1> Adopt a Pet!</h1>
  <p> Browse through the links below to find your new furry friend: </p>
  <ul>
  <li><a href ="/animals/dogs">dogs </a></li>
  <li><a href ="/animals/cats">Cats </a></li>
  <li><a href ="/animals/rabbits">Rabbits </a></li>
  </ul>
  '''
@app.route('/animals/<pet_type>')
def animals(pet_type):

  html =f'<h1>List of pets {pet_type}</h1>'

  for p in pets:
    html += "<ul>"
    if p == pet_type:
      for a,b in enumerate(pets[p]):
        #html += '<li>' + str(pets[p]) +'</li>'
        html += '<li>' + pets[p][a]['name'] +'</li>'
        #html += ' ' + str(pets) + ' '
    html += "</ul>"
  return html
 