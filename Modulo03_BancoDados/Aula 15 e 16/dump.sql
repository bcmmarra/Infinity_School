-- Criando Banco de Dados
CREATE DATABASE IF NOT EXISTS hospital;

-- Excluindo Banco de Dados
-- DROP DATABASE hospital;

-- Utilizando Banco de Dados
USE hospital;

-- Criando Tabela de Pacientes
DROP TABLE IF EXISTS pacientes;
CREATE TABLE IF NOT EXISTS pacientes (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(255) NOT NULL,
	cpf VARCHAR(11) NOT NULL UNIQUE,
	data_nascimento DATE NOT NULL,
	ativo BOOL NOT NULL DEFAULT TRUE
);

-- Alter
-- Modify
ALTER TABLE pacientes 
MODIFY data_nascimento DATETIME;

-- Adicionar uma Coluna (Add)
ALTER TABLE pacientes
ADD email VARCHAR(255);

-- Remover uma coluna
-- ALTER TABLE pacientes
-- DROP COLUMN email;

DROP TABLE IF EXISTS medicos;
CREATE TABLE IF NOT EXISTS medicos (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(255) NOT NULL,  
	crm VARCHAR(6) NOT NULL UNIQUE,
	data_nascimento DATE NOT NULL,
	ativo BOOL NOT NULL DEFAULT TRUE
);

ALTER TABLE medicos
ADD email VARCHAR(255);

CREATE TABLE IF NOT EXISTS enderecos (
	id INT PRIMARY KEY AUTO_INCREMENT,
    rua VARCHAR(255) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(2) NOT NULL,
    numero VARCHAR(10)
);

ALTER TABLE enderecos 
MODIFY numero VARCHAR(10) DEFAULT 'S/N';
