from random import sample
vetor = sample(range(100), 10)
maior = menor = vetor[0]
for x in vetor[1:]:
  if x > maior: maior = x
  if x < menor: menor = x
print ('Vetor:', vetor)
print (f'Maior: {maior}')
print (f'Menor: {menor}')



from random import sample
vetor = sample(range(100), 20)
par = [x for x in vetor if x % 2 == 0]
ímpar = [x for x in vetor if x % 2 == 1]
print ('Vetor', vetor)
print ('Pares', par)
print ('Ímpares', ímpar)



from random import sample
v1 = sample(range(100), 10)
v2 = sample(range(100), 10)
v3 = []
for x in zip(v1, v2):
  v3.extend(list(x))
print('v1:', v1)
print('v2:', v2)
print('v3:', v3)



texto = '''The Python Software Foundation and the global
   Python community  welcome  and  encourage participation
   by everyone.  Our  community is  based  on mutual respect,
   tolerance, and encouragement, and we are working to help each
   other live up to  these  principles.  We  want our  community
   to  be  more  diverse: whoever you  are,  and whatever  your
   background, we welcome  you.'''.lower()

import string
for c in string.punctuation:
  texto = texto.replace(c, ' ')
resp = [p for p in texto.split()
        if p[0] in 'python' or p[-1] in 'python']
print (resp)



texto = '''The Python Software Foundation and the global
   Python community  welcome and encourage participation
   by everyone. Our community is based on mutual respect,
   tolerance, and encouragement, and we are working to help
   each other live up to these principles. We want our
   community to be more diverse: whoever you are, and
   whatever your background, we welcome you.'''.lower()

import string
for c in string.punctuation:
  texto = texto.replace(c, ' ')
  
def pitônica(x):
  for c in x:
    if c in 'python':
      return True
  return False

resp = [p for p in texto.split()
        if pitônica(p) and len(p) > 4]
print (resp)
print (len(resp))
