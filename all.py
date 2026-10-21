
#Faça uma aplicação que receba em  °C e retorne em  °F

#pergunta = int(input("Digite a temperatura em  °C: "))
#temp = pergunta * 1.8 + 32
#print(f"A temperatura em °F é {temp}")

#------------------------------------------------------#

#Solicite 3 notas ao usuario e calcule a media entre elas
#not1 = float(input("Insira aqui a primeira nota: "))
#not2 = float(input("Aqui a segunda: "))
#not3 = float(input("Aqui a terceira: "))
#soma = not1 + not2 + not3
#media = soma / 3
#print(f"A média das notas é de {media}")

#------------------------------------------------------#

#Peça 2 numeros ao usuario e realise uma divisao dos mesmos

#num1 = float(input("Digite um numero: "))
#num2 = float(input("Digite um numero: "))
#soma = num1 / num2
#print(f"A divisão dos numeros é {soma}")

#------------------------------------------------------#

#Peça o nome e o sobrenome do usuario e mande uma mensagem de boas vindas com o seu nome e sobrenome

#perg = input("Olá, nos diga seu nome: ")
#perg2 = input("Agora nos diga seu sobrenome: ")
#print(f"Seja bem vindo {perg} {perg2}")

#------------------------------------------------------#

#dia = input("Qual o dia do seu nascimento? ")
#mes = input("E de que mês? ")
#ano = input("E por fim, de qual ano? ")
#print(f"Você nasceu no dia {dia} de {mes} de {ano} Correto?")

#------------------------------------------------------#

#n1 = int(input ("Número: "))
#n2 =  int(input("Outro: "))
#soma = n1 + n2
#print(f"A soma de {n1} + {n2} é igual a {soma}")

#------------------------------------------------------#

#n = input("Digite alguma coisa: ")
#print("O tipo primitivo desse valor é" , type(n)) 
#print("Possui apenas espaços: ", n.isspace()) 
#print("É um numero: ", n.isnumeric()) 
#print("Possui apenas letras: ", n.isalpha()) 
#print("Está tudo em maiúsculo: ", n.isupper()) 
#print("Está tudo em minúsculo: ", n.islower()) 
#print("Está capitalizado?", n.istitle()) 

#------------------------------------------------------#

#n = int (input("Digite um número: "))
#ant = n - 1
#suc = n + 1 
#print (f"O antecessor desse número é {ant} e o seu sucessor é {suc}")

#------------------------------------------------------#

#n = int (input ("Digite aqui seu número: "))
#dbr = n * 2
#trp = n * 3
#rz = n ** (1/2)
#print(f"O Dobro do seu número é {dbr}, seu triplo é {trp} e sua raiz é {rz}")

#------------------------------------------------------#

#m = int(input ("Coloque aqui a medida em metros: "))
#cm = m * 100
#mm = m * 1000
#print(f"{m} metros em centímetros equilave a {cm} e em milímetros {mm}")

#------------------------------------------------------#

#>>>>>>>>>(Que bagulho feio)<<<<<<<<<#
#n = int(input ("Digite o número inicial: "))
#x1 = n * 1
#x2 = n * 2 
#x3 = n * 3
#x4 = n * 4 
#x5 = n * 5
#x6 = n * 6
#x7 = n * 7
#x8 = n * 8 
#x9 = n * 9 
#x10 = n * 10
#print(f"{n}x1={x1}\n {n}x2={x2}\n {n}x3={x3}\n {n}x4={x4}\n {n}x5={x5}\n {n}x6={x6}\n {n}x7={x7}\n {n}x8={x8}\n {n}x9={x9}\n {n}x10={x10}")

#------------------------------------------------------#

#mny = float(input("Quantos reais você tem na sua carteira? "))
#dlr = mny / 5.75
#print(f"Com essa quantia voce por atualmente comprar {dlr: .2f} dolares!")

#------------------------------------------------------#

#a = float(input("Qual a altura da parede ? "))
#l = float(input("E a largura ? "))
#ar = a * l 
#t = ar / 2 
#print(f"Você vai precisar de {t} litros de tinta")

#------------------------------------------------------#

#v = float(input("Digite o preço do produto: "))
#d = v - (v * 5 / 100)
#print(f"Hoje, pela nossa promoção, essa peça esta com 5% de desconto e está saindo por apenas {d} reais. 😊")

#------------------------------------------------------#

#s = float(input("Qual o seu salário atualmente? "))
#a = s + (s * 15 / 100)
#print(f"Você receberá um aumento de 15% no seu salário, assim recebendo atualmente {a} reias.")

#------------------------------------------------------#

#>>>>>  60 p/ dia | 0.15 p/ km rodado  <<<<<#
#d = int(input("Por quantos dias você rodou? "))
#k = int(input("Por quanto km você rodou? "))
#ds = d * 60
#ks =  k * 0.15
#v = ds + ks 
#print(f"O valor total a ser pago é de R${v}")

#------------------------------------------------------#

import math
#num = float(input("Digite um número: "))
#res = math.trunc(num)
#print(f"A parte inteira do seu numero é {res}")

#------------------------------------------------------#

#co = int(input("Cateto oposto: "))
#ca = int(input("Cateto adjacente: "))
#hip = math.hypot(co, ca)
#print(f"A sua hipotenusa é {hip: .2f}")

#------------------------------------------------------#

#angl = int(input("Digite aqui o ângulo: "))
#rad = math.radians(angl)
#se = math.sin(rad)
#co = math.cos(rad)
#tan = math.tan(rad)
#print(f"O seu seno é {se: .1f}, seu cosseno é {co: .1f} e sua tangente é {tan: .1f}")

#------------------------------------------------------#

import random
#nm1 = input("Insira o nome do aluno: ")
#nm2 = input("Segundo nome: ")
#nm3 = input("Terceiro aluno: ")
#nm4 = input("Quarto aluno: ")
#al = [nm1, nm2, nm3, nm4]
#srt = random.choice(al)
#print(f"O aluno escolhido é {srt}! ")

#------------------------------------------------------#

# random.shuffle(nomes) enumerate(nomes, start=1)

#n1 = input("Nome aluno: ")
#n2 = input("Nome aluno: ")
#n3 = input("Nome aluno: ")
#n4 = input("Nome aluno: ")
#all = [n1, n2, n3, n4]
#sort = random.shuffle(all)
#print("A ordem será ")
#print(all)

#------------------------------------------------------#

#idade = int(input("Informe sua idade: "))
#if idade >= 18:
#    print("Pode entrar!")
#else:
#    print("Rapa fora!")

#------------------------------------------------------#

#salario = float(input("Informe o salário: "))
#if salario <= 3000:
#    print("Junior")
#elif salario > 3000 and salario <= 6000:
#    print("Pleno")
#elif salario > 6000 and salario <= 15000:
#    print("Senior")
#else:
#    print("Gerente")

#------------------------------------------------------#

#nome = input("Digite seu nome completo: ")
#print(nome.upper())
#print(nome.lower())
#print(len(nome.replace (" ", "")))
#separado = nome.split()
#print(len(separado[0]))

#------------------------------------------------------#

#numero = input("Digite um numero de 0 a 9999: ")
#print("Unidade", numero[3])
#print("Dezena", numero[2])
#print("Centena", numero[1])
#print("Milhar", numero[0])

#------------------------------------------------------#

#cidade = input("Digite aqui o nome da sua cidade: ").strip()
#print(cidade[:5].upper() == "SANTO")

#------------------------------------------------------#

#nome = input("Digite aqui seu nome completo: ").strip()
#print("SILVA" in nome.upper)

#------------------------------------------------------#

#frase = input("Digite uma frase qualquer: ").strip().upper()
#print(f"Sua frase possui {frase.count("A")} letra(s) 'a' ")
#print(f"A letra a aparece pela primeira vez na {frase.find("A")+1} posição")
#print(f"A ultima letra 'a' apareceu na posição {frase.rfind("A")+1}")

#------------------------------------------------------#

#nome = input("Digite aqui seu nome completo: ").strip()
#app = nome.split()
#print(f"Seja bem vindo {app[0]} {app[len(app)-1]}")

#------------------------------------------------------#

#nmsrt = random.randint(0,5)
#num = int(input("Chute um número: "))
#if num == nmsrt:
#    print("Parabéns, você acertou!🎉🎉")
#else:
#    print("Você errou, tente novamente 🙁")
#    print(nmsrt)

#------------------------------------------------------#

#km = int(input("A qual velocidade o carro estava? "))
#if km >= 80:
#    multa = (km - 80)*7
#    print(f"A multa a ser paga será de R${multa: .2f}!")
#else:
#    print("Nenhum multa a ser aplicada, tenha um bom dia!")

#------------------------------------------------------#

#num = int(input("Digite um número: "))
#if num % 2 == 0:
#    print(f"O número {num} é par!")
#else:
#    print(f"O número {num} é ímpar!")

#------------------------------------------------------#

#km = int(input("A quantos km fica o seu destino? "))
#if km <= 200:
#    preço = km * 0.50
#    print(f"Sua viagem custará R${preço: .2f}")
#else: 
#    preço = km * 0.45
#    print(f"Sua viagem custará R${preço: .2f}")

#------------------------------------------------------#

import datetime
#ano = int(input("Digite um ano: , ou digite 0 para analisar o ano atual: "))
#if ano == 0:
#    ano = datetime.date.today().year
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#    print(f"O ano de {ano} é bissexto!")
#else:
#    print(f"O ano de {ano} não é bissexto")

#------------------------------------------------------#

#n1 = int(input("Digite o primeiro valor: "))
#n2 = int(input("Digite o segundo valor: "))
#n3 = int(input("Digite o terceiro valor: "))
#nm = [n1, n2, n3]
#if n1<n2 and n1<n3:
#    menor = n1
#if n2<n1 and n2<n3:
#    menor = n2
#if n3<n1 and n3<n2:
#    menor = n3
#print(f"O menor número digitado foi {menor}.")
#if n1>n2 and n1>n3:
#    maior = n1
#if n2>n1 and n2>n3:
#    maior = n2
#if n3>n1 and n3>n2:
#    maior = n3
#print(f"O maior número digitado foi {maior}.")

#------------------------------------------------------#


##aumento = salário + (salário * 15 / 100) Calculo de %
#sala = float(input("Qual seu salário atualmente? "))
#if sala <= 1250.00:
#   au = sala + (sala * 15 / 100)
#   print(f"Você ira receber um aumento de 15%, passando assim a ganhar R${au: .2f}")
#else: 
#    au1 = sala + (sala * 10 / 100)
#    print(f"Você ira receber um aumento de 10%, passando assim a ganhar R${au1: .2f}")

#------------------------------------------------------#

#O conceito aqui é que se somar duas partes elas derem um número mais que a terceira parte então
# pode formar um trinângulo
#r1 = float(input("Primeira medida: "))
#r2 = float(input("Segunda medida: "))
#r3 = float(input("Terceira medida: "))
#if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
#    print("As medidas podem formar um triângulo!")
#else:
 #   print("As medidadas não podem formar um trinângulo!")

 #------------------------------------------------------#

#print("\033[1;32m-=-=-=-= Empréstimo para casa =-=-=-=-\033[m")
#cs = int(input("Qual o valor da casa ? "))
#sl = int(input("Quanto você recebe ? "))
#an = int(input("Em quantos anos pretende pagar ? "))
#mses = an * 12
#ndp = cs / mses
#pctgn = (30 / 100) * sl
#if ndp >= pctgn:
#    print("\033[1;31mEmpréstimo negado, por falta de verba.\033[m")
#else:
#    print("\033[32mEmpréstimo aprovado!!!\033[m")
#    print(f"Você ira pagar em {mses} parcelas de R${ndp} cada.")

 #------------------------------------------------------#

#nm = int(input("Digite um número qualquer: "))
#per = input("Qual base de conversão deseja usar ? \n 1 - binário \n 2 - octal \n 3 - hexadecimal \n Digite aqui sua resposta: ")
#if per == "1":
#   bi = bin(nm)
#   print(bi)
#elif per == "2":
#    oc = oct(nm)
#    print(oc)
#else:
#    hx = hex(nm)
#    print(hx)

 #------------------------------------------------------#

#n1 = int(input("Digite um número: "))
#n2 = int(input("Digeite um segundo número: "))
#if n1 > n2:
#    print(f"O número {n1} é maior que número {n2}.")
#elif n1 < n2:
#    print(f"O número {n2} é maior que número {n1}.")
#else:
#    print("Não tem número maior, eles tem o mesmo valor.") 

 #------------------------------------------------------#

#ano = int(input("Em que ano você nasceu meu jovem? "))
#ano_atual = datetime.date.today().year
#idade = ano_atual - ano
#if idade < 18:
#   ano_falta = 18 - idade
#   print(f"\033[33mAinda não chegou a hora do seu alistamento, faltam {ano_falta} anos para você se alistar.\033[m")
#elif idade == 18:
#    print(f"\033[1;32mChegou a hora do seu alistamento!!!\033[m")
#elif idade > 18:
#    ano_atraso = idade - 18
#    print(f"\033[31mJá passou da hora do seu alistamento, se passaram {ano_atraso} anos do prazo.\033[m")

 #------------------------------------------------------#

#n1 = float(input("Digite aqui a primeira nota: "))
#n2 = float(input("Digite aqui a segunda nota: "))
#media = (n1 + n2) / 2
#if media < 5.0:
#    print("\033[1;31mREPROVADO!!!\033[m")
#elif media > 5.0 and media <= 6.9:
#    print("\033[4;33mEm recuperação.\033[m")
#elif media >= 7.0:
#    print("\033[32mAprovado!\033[m")

 #------------------------------------------------------#

#idade = int(input("Digite a idade do atleta: "))
#if idade <= 9:
#    print("Mirim")
#elif idade > 9 and idade <= 14:
#    print("Infantil")
#elif idade > 14 and idade <= 19:
#    print("Junior")
#elif idade == 20:
#    print("Sênior")
#else: print("Master")

 #------------------------------------------------------#

#r1 = float(input("Primeira medida: "))
#r2 = float(input("Segunda medida: "))
#r3 = float(input("Terceira medida: "))
#if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
#    print("As medidas podem formar um triângulo ", end="")
#    if r1 == r2 and r1 == r3:
#        print("equilátero.")
#    elif r1 != r2 != r3 != r1:
#        print("escaleno.")
#    else:
#        print("isósceles")
#else:
#   print("As medidadas não podem formar um trinângulo!")

 #------------------------------------------------------#

#peso = float(input("Qual seu peso? "))
#altura = float(input("Qual sua altura? "))
#imc = peso / (altura ** 2)
#if imc < 18.5:
#    print("Você está abaixo do peso.")
#elif imc >= 18.5 < 25:
#    print("Você está no peso ideal.")
#elif imc == 25 < 30:
#    print("Você está com sobrepeso.")
#elif imc == 30 <=40:
#    print("Você está com obesidade.")
#else:
#    print("Você está com obesidade mórbida.")

 #------------------------------------------------------#

#preço = float(input("Qual o preço do produto? "))
#pagamento = input("Qual a forma de pagamento? \n \033[36m1 - Á vista no pix/dinheiro:\033[m \n \033[32m10% de desconto\033[m \n \033[36m2 - Á vista no cartão:\033[m \n \033[32m5% de desconto\033[m \n \033[36m3 - Em até 2x no cartão:\033[m \n \033[33mPreço normal\033[m \n \033[36m4 - 3x ou mais no cartão:\033[m  \n \033[31m20% de juros\033[m \n Selecione sua opção: ")
#if pagamento == "1":
#   pg = preço - (preço * 10 / 100)
#    print(f"O total a pagar será R${pg}")
#elif pagamento == "2":
#    pg = preço - (preço * 5 / 100)
#    print(f"O total a ser pago é de R${pg}")
#elif pagamento == "3":
#    print(f"O valor final ficou em R${preço}")
#else:
#    pg = preço + (preço * 30 / 100)
#    print(f"O Preço final do produto ficou em R${pg}")

 #------------------------------------------------------#

import time 
#itens = ("Pedra", "Papel", "Tesoura")
#print("\033[31m=-=-=-=-=-Faça sua jogada-=-=-=-=-=\033[m")
#print(" \033[35m[ 0 ] Pedra 🪨 \n [ 1 ] Papel 📃 \n [ 2 ] Tesoura ✂️\033[m")
#res = int(input("Sua jogada: "))
#print("\033[31mJO\033[m")
#time.sleep(1)
#print("\033[33mKEN\033[m")
#time.sleep(1)
#print("\033[32mPO!!!\033[m")
#maquina = random.randint(0, 2)
#print("-=" *15)
#print(f"Você escolheu {itens[res]}")
#print(f"O sistema escolheu {itens[maquina]}")
#print("-=" *15)

#if maquina == 0:
#    if res == 0:
#        print("\033[33mEMPATE.\033[m")
#    elif res == 1:
#        print("\033[32mVOCÊ VENCEU!\033[m")
#    elif res == 2:
#        print("\033[31mO SISTEMA VENCEU!!!\033[m")
#    else:
#        print("JOGADA INVÁLIDA!\033[m")
#if maquina == 1:
#    if res == 0:
#        print("\033[31mO SISTEMA VENCEU!!!\033[m")
#    elif res == 1:
#        print("\033[33mEMPATE.\033[m")
#    elif res == 2:
#        print("\033[32mVOCÊ VENCEU!\033[m")
#    else:
#        print("JOGADA INVÁLIDA!\033[m")
#if maquina == 2:
#    if res == 0:
#        print("\033[32mVOCÊ VENCEU!\033[m")
#    elif res == 1:
#        print("\033[31mO SISTEMA VENCEU!!!\033[m")
#    elif res == 2:
#        print("\033[33mEMPATE.\033[m")
#    else:
#        print("JOGADA INVÁLIDA!")
        
 #------------------------------------------------------#

#print("---------- Contagem fogos ----------")
#for c in range(10, -1, -1):
#    print(c)
#    time.sleep(1)
#print("BOOOOOOOOM!!!!!!🎆🎆🎆")


#print("Os números pares entre 0 e 50 são:")
#for c in range(0, 51, 2):
#    print(c)

#soma = 0
#cont = 0
#for c in range(1, 500, 2):
#      if c % 3 == 0:
#        cont = cont + 1
#        soma = soma + c
#print(f"A soma de todos os {cont} valores é igual a {soma}.")

#-----------------------------------------------------#

#Refazendo linha 83#
#Agora sim !!!#
#num = int(input("Digite o número: "))
#for c in range(1, 11):
#    print(f"{num} x {c} = {num*c}")

#soma = 0
#for c in range(1, 7):
#   num = int(input("Digite um valor: "))
#    if num % 2 == 0:
#        soma = soma + num
#print(soma)

#-----------------------------------------------------#

#formula PA > An = A1 + (n - 1) x r
#ter = int(input("Digite o primeiro termo: ")) #a1
#rz = int(input("Digite a razão: ")) #r
#dez = ter + (10 - 1) * rz
#for c in range(ter, dez + rz , rz):
#    print(f"{c}", end=' - ')
#print("Fim.")

#-----------------------------------------------------#

#----primo = divide somente por 1 e ele mesmo----#
#total = 0
#num = int(input("Digite um número: "))
#for c in range(1, num + 1):
#    if num % c == 0:
#        total += 1

#if total == 2:
#    print("Seu número é primo")
#else:
#    print("Seu número não primo")

#-----------------------------------------------------#

#frase = input("Digite um frase: ").strip().lower()
#palavras = frase.split()
#junto = "".join(palavras)
#red = ""
#for letra in range(len(junto) -1, -1, -1):
#    red += junto[letra]
#if red == junto:
#    print(f"O inverso de --{frase}-- é --{frase}--.")
#    print("Sua frase é um palíndromo!")
#else:
#    print("Sua frase não é um palíndromo.")

#-----------------------------------------------------#

#totmaior = 0
#totmenor = 0
#for c in range(1, 8):
#    ano = int(input("Digite o ano de nascimento: "))
#    idade = 2025 - ano 
#   if idade >= 21:
#       totmaior += 1
#
#    else:
#        totmenor += 1
#print(f"Temos ao total {totmaior} pessoas maior de idade.")
#print(f"E {totmenor} pessoas menor de idade.")

#-----------------------------------------------------#

#menor = 0
#maior = 0
#for c in range (1, 6):
#   peso = float(input("Digite o aqui o peso em kg: "))
#   if c == 1:
#      maior = peso
#      menor = peso
#   else:
#      if peso > maior:
#         maior = peso
#      if peso < menor:
#         menor = peso 
#print(f"O maior peso é de {maior}")
#print(f"O menor peso foi de {menor}")   

#-----------------------------------------------------#  

#med = 0
#Nvelho = ""
#totF = 0
#for c in range(1, 5):
#    nome = input("Digite o nome: ")
#    idade = int(input("Digite a idade: "))
#    sexo = input("Sexo M/F: ")
#    if c == 1 and sexo in "Mm":
#        Hvelho = idade
#        Nvelho = nome
#    if sexo in "Mm" and idade > Hvelho:
#        Hvelho = idade
#        Nvelho = nome 
#    if sexo in "Ff" and idade <20:
#        totF += 1
#
#    med += idade 
#    medf = med / 4
#print(f"A idade média do grupo é {medf: .1f}.")
#print(f"O Homi mais velho tem {Hvelho} anos e é o {Nvelho}")
#print(f"São {totF} novinhas")

#-----------------------------------------------------#

#sexo = input("Digite aqui seu sexo: ")
#while sexo != "M" or "F".upper:
#    print("Sexo inválido  digitado")
#if sexo == "M" or "F":
#    print("Fim")