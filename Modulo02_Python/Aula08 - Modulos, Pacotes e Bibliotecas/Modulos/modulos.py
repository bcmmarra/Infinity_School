# Módulos nativos do Python (também chamados de built-in modules)
# OS (Manipula o Sistema Operacional)
import os
os.system('mkdir minha_pasta') # Cria uma pasta na Raiz do Diretório

import random
print(random.randint(1, 20))
print(random.choice(['Bruno', 'Camila', 'João Pedro', 'Davi', 'Gigi']))

# Módulos criados por nós (locais)
# ✅ 1. Importando o módulo inteiro
print('✅ 1. Importando o módulo inteiro')
import letras

resultado = letras.contar_vogais("Programar é incrível!")
print(resultado)

# 🧩 2. Importando funções específicas
print('🧩 2. Importando funções específicas')
from letras import contar_vogais, contar_total_vogais

texto = "O rato roeu a roupa do rei de roma"

print(contar_vogais(texto))
print(contar_total_vogais(texto))

# 🚫 3. Importando tudo do módulo (não recomendado)
print('🚫 3. Importando tudo do módulo (não recomendado)')
from letras import *

print(contar_vogais("ChatGPT"))
print(contar_total_vogais("FastAPI"))

# 💬 Dica Extra: Renomeando um módulo
print('💬 Dica Extra: Renomeando um módulo')
import letras as lt

print(lt.contar_vogais("Modularização é poder!"))