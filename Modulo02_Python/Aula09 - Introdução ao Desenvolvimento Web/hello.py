from flask import Flask

# Criando nossa aplicação Flask
app = Flask(__name__)

# Aqui estamos criando uma rota
@app.route('/')
def hello():
    return {'messagem': 'Hello World'}

# Retornando um Texto
@app.route('/text')
def endpoint_text():
	return 'Retornando um Texto Plano'

# Retornando um JSON
@app.route('/json')
def endpoint_api():
	return {'message': 'Aqui temos um JSON'}

# Aqui estamos executando a aplicação
app.run(debug=True)
