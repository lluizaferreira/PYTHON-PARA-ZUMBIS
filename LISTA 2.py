#Exercicio 1
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a < b + c or b < a + c or c < a + b:
    print('Esta figura pode ser um triângulo')
if a == b == c:
    print('É um triângulo equilátero')
if  a == b != c or b == a != c or c == b != a or c == a != b:
    print('É um triângulo isósceles')
elif a != b != c:
    print('É um triângulo escaleno')

#Exercicio 2
    print ('Insira um ano para saber se é/ou será bissexto:  ')
a = int(input('Ano: '))
if a  % 4 == 0 and (a % 100 != 0 or year % 400 == 0):
    print ('Bissexto')
else:
    print ('Nao bissexto')

#Exercicio 3
p = float(input('Peso dos peixes kg:   '))
if p > 50:
    excesso = p - 50
    multa = excesso * 4
    print (f'O excesso de peso é {excesso} kg:  ')
    print (f'A multa é de R$ {multa:.2f}:  ')
else:
    print ('ZERO')

#Exercicio 4
n1 = int(input('Insira um número 1: '))
n2 = int(input('Insira um número 2:  '))
n3 = int(input('Insira um número 3:  '))

if n1 > n2 and n1>  n3:
    print ('O número maior é o:  ', n1)
elif n2 > n1 and n2> n3:
    print ('O número maior é o:  ', n2)
elif n3 > n1 and n3> n2:
    print ('O número maior é o:  ', n3)

#Exercicio 5
n1 = int(input('Insira um número 1: '))
n2 = int(input('Insira um número 2:  '))
n3 = int(input('Insira um número 3:  '))

if n1 > n2 and n1>  n3:
    print ('O número maior é o:  ', n1)
elif n2 > n1 and n2> n3:
    print ('O número maior é o:  ', n2)
elif n3 > n1 and n3> n2:
    print ('O número maior é o:  ', n3)


if n1 < n2 and n1 <  n3:
    print ('O número menor é o:  ', n1)
elif n2 < n1 and n2 < n3:
    print ('O número menor é o:  ', n2)
elif n3 < n1 and n3 < n2:
    print ('O número menor é o:  ', n3)

#Exercicio 6
s = float(input('Insira seu salário por hora R$: '))
h = int(input('Insira o número de horas trabalhadas durante o mes: '))
a = s * h
print (f'O valor do salário bruto mensal é de R$: {a:.2f} ')
b = a * 0.11
print (f'O desconto do IR é de R$: {b:.2f} ')
c = a * 0.08
print (f'O desconto do INSS é de R$: {c:.2f} ')
d = a * 0.05
print (f'O desconto do sindicato é de R$: {d:.2f} ')
e = a - b - c - d
print (f'O salário líquido é de R$: {e:.2f} ')


#Exercicio 7
area = int(input('Area total a ser pintada: '))
qt = int(((area / 3) / 18) + 1)
print (f'Total de latas a serem usadas: ',qt)
preco = 80 * qt
print (f'O preco total é de R$ {preco:.2f}: ')
           
