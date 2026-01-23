-- Select - Buscar Registros
SELECT * FROM pacientes;

SELECT
	id,
    nome,
    cpf,
    data_nascimento,
    ativo
FROM
	pacientes
-- WHERE
-- ativo = 1 AND YEAR(data_nascimento) < 1990;
ORDER BY
	data_nascimento DESC;
-- ASC = Ascendente
-- DESC = Descendente


-- Insert - Adicionar Registros
INSERT INTO pacientes(nome, cpf, data_nascimento)
VALUES ('Natan', '12345678912', '1996-02-17');

INSERT INTO pacientes(nome, email, cpf, data_nascimento)
VALUES ('Davi', 'davi@email.com', '12345678900', '1998-05-17');

INSERT INTO pacientes(nome, email, cpf, data_nascimento)
VALUES ('Giovanna', 'gigi@email.com', '12345670000', '2021-05-02'),
	   ('Bruno', 'bcm@email.com', '12345000000', '1990-05-01');

INSERT INTO pacientes(nome, email, cpf, data_nascimento, ativo)
VALUES ('Davi', 'davi@email.com', '12345670900', '1900-05-17', FALSE);

-- Update - Atualizar Registros
UPDATE pacientes
SET email = 'natan@gmail.com',
	data_nascimento = '1989-05-10'
WHERE id = 1; -- OBRIGATÓRIO para indicar onde inserir a atualizar, caso contrário ele vai atualizar TODAS as linhas da Coluna modificada.

-- Delete - Excluir Registros
DELETE FROM pacientes WHERE id = 5;

-- DELETE FROM pacientes WHERE cpf = '12345670900' OR ativo = FALSE;
-- OBRIGATÓRIO o uso WHERE para indicar qual linha DELETAR, caso contrário ele vai DELETAR TUDO.
