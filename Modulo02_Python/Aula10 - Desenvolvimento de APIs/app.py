import uuid # Gera o ID automatico e unico.
from flask import Flask, request 
from http import HTTPStatus

animais = [
	{
		'id': str(uuid.uuid4()),
		'nome': 'Café',
		'especie': 'Gato'
	},
	{
		'id': str(uuid.uuid4()),
		'nome': 'Margot',
		'especie': 'Gato'
	},
]
app = Flask(__name__) 
app.json.sort_keys = False

#Quando não passamos o methods, por padrão ele coloca somente o método GET methods=['GET], buscar
@app.route('/animais', methods=['GET'])
def listar_animais():
	if len(animais) == 0:
		return ('', HTTPStatus.NO_CONTENT)

	return (animais, HTTPStatus.OK)

@app.route('/animais', methods=['POST'])
def cadastrar_animal():
	data = dict(request.get_json()) # Converter o json em Dicionário
#	animais.append(data) #Nunca devemos pegar a resposta em adicionar direto no nosso Banco de Dados, sempre devemos tratar e validar as informações.

	if data.get('nome') is None: # Validação se o campo nome foi enviado. 
		return (
			{'message': 'O campo \"nome\" é obrigatório'},
			HTTPStatus.BAD_REQUEST
		)

	if data.get('especie') is None: # Validação se o campo nome foi enviado. 
		return (
			{'message': 'O campo \"especie\" é obrigatório'},
			HTTPStatus.BAD_REQUEST
		)
	
	# Após verificar se os campos esperados foram recebidos, selecionamos os campos que queremos adicionar ao nosso banco de dados, pois quem esta enviando os dados podem enviar dados desnecessarios.
	animal = {
		'id': str(uuid.uuid4()),
		'nome': data.get('nome'),
		'especie': data.get('especie')
	}

	animais.append(animal) # Aqui já tratamos as informação recebidas e adicionamos no nosso Banco de Dados.
	return {'messagem': 'Animal cadastrado com sucesso'}














if __name__ == '__main__':
    app.run(debug=True)