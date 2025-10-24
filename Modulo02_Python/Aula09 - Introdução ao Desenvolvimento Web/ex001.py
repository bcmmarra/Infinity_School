from flask import Flask

pessoas = [
    {
        'id': '1',
        'nome': 'Bruno',
        'idade': 33
    },
    {
        'id': '2',
        'nome': 'Camila',
        'idade': 33
    },
    {
        'id': '3',
        'nome': 'Giovanna',
        'idade': 4
    }
]

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/pessoas')
def listar_pessoas():
    return pessoas

app.run(debug=True)
