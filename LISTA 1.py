# Exercicio 1
n1 = int(input( '1o número: '))
n2 = int(input( '2o número: '))
print (n1+n2)

# Exercicio 2
m = int(input( 'Metros: '))
print (f'Milímetros:  {m*1000}')

# Exercicio 3
d = int(input('Dias: '))
h = int(input('Horas:'))
m = int(input('Minutos: '))
s = int(input('Segundos: '))
total = d*24*60*60 + h*60*60 + m*60 + s
print (total)

# Exercicio 4
salario = float(input('Qual valor do seu salário? R$'))
porc = int(input('Qual foi a porcentagem de aumento do seu salário? %'))

porctotal = porc / 100;
calcporc = salario * porctotal;
salfinal = salario + calcporc;

print('Seu aumento será de R$: ', calcporc, '\n',
'O valor atual do seu salario sera de R$: ',salfinal);

# Exercicio 5
merc = float(input('Informe o valor da mercadoria R$'))
desc = int(input('Informe o valor do desconto %'))

desctotal = desc / 100;
calcdesc = merc * desctotal;
valorfinal = merc - calcdesc;

print('O valor total será de R$: ', calcdesc , '\n',
'O preço a pagar será de R$: ',valorfinal)

# Exercicio 6
dist = int(input('Informe a distancia a ser percorrida em km/h: '))
vel = int(input('Informe a velocidade media: '))

tempo = dist / vel
print ('O tempo necessario para essa viagem sera de: ',tempo,'horas.')

# Exercicio 7
C = int(input('Insira a temperatura em graus para conversao em fahrenheit: '))
F = (9*C)/5+32
print ('O valor em fahrenheit é de: ',F)

# Exercicio 8
F = int(input('Insira a temperatura em fahrenheit para conversao em graus: '))
C = (5*(F-32) / 9
print ('O valor em graus é de: ',C)

# Exercicio 9
kmper = int(input('Quantos km foram percorridos? '))
dias = int(input ('Quantos dias o carro foi utilizado? '))
km = 0,18
dia = 60,00
a = kmper * km
b = dias * dia
pt = a + b
print ('O valor total a ser pago é de R$: ',pt)

# Exercicio 10
a = int(input ('Informe a quantidade de cigarros fumados por dia '))
b =  a * 365
c = int(input ('Informe a quantidade de anos perdidos pelo uso do cigarro '))
d = b * c * 10 / 1440
print ('A quantidade de dias perdidos pelo uso do cigarro é de: ',d)

# Exercicio 11
print ('2 elevado a 1 milhão tem %d digitos' %len(str(2**1000000)))

     
