#Exercicio 1
conta = int(input('Valor total da conta: '))
pagamento = int(input('Pagamento efetuado de: '))
caixa = [50, 20, 10, 5, 2, 1]
troco = pagamento - conta
for notas in caixa:
    if troco >= notas:
        quantidade = troco / notas
        r = troco - (notas * int(quantidade))
        print(int(quantidade),'notas de R$',notas)
        troco = r

#Exercicio 2
usuario = input('Coloque um nome de usuário: ')
senha = input('Coloque uma senha: ')
while usuario==senha:
    print('usuario e senha invalidos, tente novamente ')
    usuario = input('Coloque um nome de usuário: ')
    senha = input( 'Coloque uma senha: ')
print ('Seja bem vindo!')

#Exercicio 3
a = 8000
b = 200000
ano = 0

while a <= b:
    a += a * 0.03
    b += b * 0.015
    ano += 1

print ('A ultrapassa ou iguala a B em %d anos' %ano)

#Exercicio 4
n = int(input('Que termo deseja encontrar: ')) 
ultimo=1
penultimo=1 
if (n==1) or (n==2): 
     print('1') 
else: 
     count=3 
while count <= n: 
     termo = ultimo + penultimo
     penultimo = ultimo
     ultimo = termo
     count += 1
     print(termo)

#Exercicio 5
n1 = int(input('Primeiro número: '))
n2 = int(input( 'Segundo número: '))
if n1 < n2:
    n1, n2 = n2, n1

r1, mdc = n1%n2, n2
while r1 != 0:
    r1, mdc = mdc%r1, r1

print('O mdc de (%d,%d) é: %d'%(n1,n2,mdc))

