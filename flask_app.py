from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<p>antwoord op vraag 4 Er word een branch met de naam main aangemaakt git switcht direct naar die branch</p>"
