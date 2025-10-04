'''
Você foi contratado como desenvolvedor para criar um programa que verifique a senha digitada pelos usuários. O programa deve solicitar ao usuário que digite uma senha e verificar se ela atende aos critérios estabelecidos. Os critérios são os seguintes:
 •A senha deve ter no mínimo 8 caracteres e no máximo 12 caracteres
 '''
print("---- Validação de Senha ----")
senha = input("Digite sua senha: ")

letra = 0
for c in senha:
    letra += 1
        
if letra < 8 or letra > 12:
    print("A senha precisa ter no mínimo 8 caracteres e no máximo 12 caracteres")
            
print("---- Usuário Logado com Sucesso ----")

print("---- FIM - Validação de Senha ----")