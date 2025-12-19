-- Criando banco de dados
-- Para executar vocês podem apertar CTRL + ENTER com 
-- o cursor no comando

-- Criando o BD
# Comando para criar um BD
CREATE DATABASE hospital;

# Comando para criar um BD se não existir
CREATE DATABASE IF NOT EXISTS hospital;

# ---------------------------------------------------------------------------------------------

-- Selecionar o banco de dados hospital para USAR.
USE hospital;

# ---------------------------------------------------------------------------------------------

-- Criando a Tabela
-- Pacientes Tabela e Dados (NOME da Coluna - TIPO da Coluna - RESTRIÇÕES (caracteristicas) da Coluna
CREATE TABLE paciente (
	id INT PRIMARY KEY AUTO_INCREMENT, -- Toda coluna deve ter uma chave primaria.medicosmedicos
	nome VARCHAR(255) NOT NULL,
	cpf VARCHAR(11) NOT NULL UNIQUE,
	data_nascimento DATE NOT NULL,
	ativo BOOL NOT NULL DEFAULT TRUE
);

# -- COMANDO PARA ALTERAÇÕES - ALTER
-- Renomear a TABELA.
ALTER TABLE paciente RENAME TO pacientes;

-- Renomear o nome da COLUNA.
ALTER TABLE pacientes RENAME COLUMN data_nascimento TO dataNascimento;

# -- COMANDO PARA ALTERAÇÕES - MODIFY
ALTER TABLE pacientes
MODIFY data_nascimento  DATETIME;

-- Adicionar NOVA COLUNA
ALTER TABLE pacientes
ADD email VARCHAR(255);

-- Remover uma COLUNA
ALTER TABLE pacientes
DROP COLUMN email;

-- Inserir Dados
INSERT INTO pacientes (nome, cpf, data_nascimento)
VALUES ('Paciente1', '12334545677', '1993-01-20');

INSERT INTO pacientes (nome, cpf, data_nascimento)
VALUES ('Paciente2', '94453475655', '2000-04-20'),
		('Paciente3', '12334545678', '1993-01-20');

-- Consultar os Dados
SELECT * FROM pacientes;

# 1 - Crie uma tabela chamada “medico” ou “medicos” que deve armazenar os dados: nome, data_nascimento, ativo, crm
CREATE TABLE medicos (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    data_nascimento DATE NOT NULL,
    ativo BOOL NOT NULL DEFAULT TRUE,
    crm VARCHAR(6) NOT NULL UNIQUE
);

-- Adicionar NOVA COLUNA
ALTER TABLE medicos
ADD email VARCHAR(255);

-- Adicionar nova coluna

# 2 - Cadastre 3 médicos no banco de dados passando somente as informações obrigatórias.
INSERT INTO medicos (nome, data_nascimento, crm)
VALUES ('Camila', '1989-12-07', '78548'),
		('Bruno', '1990-05-01', '1906'),
		('Pedro', '1985-11-10', '0707');

# 3 - Faça uma consulta para buscar todos os médicos cadastrados.
SELECT * FROM medicos;

# 4 - Dado a tabela de pacientes que foi criada no material, cadastre 3 pacientes no banco de dados passando somente as informações obrigatórias.
INSERT INTO pacientes (nome, cpf, data_nascimento)
VALUES ('Camila', '00000000011', '1989-12-07'),
       ('Giovanna', '00000000111', '2021-05-02'),
       ('João', '12345678910', '1980-02-20');

# 5 - Faça uma consulta para buscar todos os pacientes cadastrados.
SELECT * FROM pacientes;

# 6 - Cadastre 2 médicos que estejam desativados no banco de dados passando todas as colunas (exceto id).
INSERT INTO medicos (nome, data_nascimento, crm, ativo)
VALUES ('Camila', '1989-12-07', '78549', FALSE),
		('Bruno Marra', '1990-05-01', '1905', TRUE),
        ('Davi', '1979-08-21', '1506', FALSE);

# 7 - Faça uma consulta para buscar todos os médicos inativos no banco de dados.
SELECT * FROM medicos
WHERE ativo = 0;

CREATE TABLE IF NOT EXISTS enderecos (
	id INT PRIMARY KEY AUTO_INCREMENT,
    rua VARCHAR(255) NOT NULL,
    bairro VARCHAR(255) NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    uf VARCHAR(2) NOT NULL
);
ALTER TABLE enderecos ADD numero VARCHAR(10);

# EXCLUIR o BD completo
DROP DATABASE hospital;