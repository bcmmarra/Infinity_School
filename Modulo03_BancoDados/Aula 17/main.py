import pacientes
from datetime import date

# Adicionar um novo paciente
novo_paciente = pacientes.adicionar_paciente(
    nome='Ana Maria',
    cpf='98765432100',
    data_nascimento=date(1990, 5, 15)
)
print('Novo paciente adicionado:', novo_paciente)


lista_de_pacientes = pacientes.listar_pacientes()
for paciente in lista_de_pacientes:
    print(paciente['id'] , paciente['nome'])
