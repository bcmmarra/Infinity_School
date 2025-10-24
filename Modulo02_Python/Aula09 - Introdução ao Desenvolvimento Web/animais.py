from flask import Flask 
from http import HTTPStatus

animais = [
	{
		'id': 1,
		'nome': 'Café',
		'especie': 'Gato'
	},
	{
		'id': 2,
		'nome': 'Margot',
		'especie': 'Gato'
	},
]

app = Flask(__name__) 
app.json.sort_keys = False

@app.route('/animais')
def listar_animais():
	if len(animais) == 0:
		return ('', HTTPStatus.NO_CONTENT)

	return (animais, HTTPStatus.OK)
	
app.run(debug=True)