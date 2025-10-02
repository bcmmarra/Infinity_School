'''Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''


diasemana = int(input("Digite um númeo que corresponde a uma dia de semana: "))

match diasemana:
    case 1:
        print("Domingo - Final de semana esta acabando")
    case 2:
        print("Segunda-Feira - Bora começar a semana")
    case 3:
        print("Terça-Feira - Todo gás")
    case 4:
        print("Quarta-Feira - Final de semana nunca chega")
    case 5:
        print("Quinta-Feira - Dia do CURSO de PYTHON")
    case 6:
        print("Sexta-Feira - Sextou com CURSO DE HTML e CSS Avançado (Super Módulo)")
    case 7:
        print("Sábado - Graças a Deus, FINAL DE SEMANA")
    case _:
        print("Valor Inválido digite entre (1 e 7).")

