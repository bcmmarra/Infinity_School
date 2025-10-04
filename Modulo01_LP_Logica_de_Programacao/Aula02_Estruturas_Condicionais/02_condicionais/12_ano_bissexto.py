'''
Faça um programa que peça um ano para o usuário e informe se o ano é bissexto ou não.

Regra: Para que o ano seja bissexto ele deve ser divisivel por 4 e não pode ser divisivel por 100, exceto se também for divisivel por 400

A primeira regra é verificar se o ano é divisível por 4. Se ele não for, você já pode dizer que ele não é bissexto. Por exemplo, anos como 2021 ou 2023 não são bissextos.

Se o ano for divisível por 4, você precisa fazer mais uma verificação.
A segunda regra é checar se ele também é divisível por 100.

Se ele for divisível por 100 (como 1900 ou 2100), você tem que fazer mais um teste: ver se ele é divisível por 400.
Se for, ele é bissexto. Se não, ele não é bissexto.

Se ele for divisível por 4, mas não for divisível por 100 (como 2024), então ele é bissexto.

'''
ano = int(input('Digite um ano: '))

if (ano % 4 == 0 and ano % 100 > 0) or ano % 400 == 0:
    print(f'O ano {ano} é Bisexto')
else:
    print(f'O ano {ano} não é Bisexto')
    