def fib(n): #Retorna uma lista todos os números de Fibonacci menores ou iguais que n ou maiores ou iguais à 1
    l = [0,1]
    i=1
    while(l[i] < n):
        l.append(l[i]+l[i-1])
        i = len(l)-1
    return l

x = input("x=")

if(not x.isnumeric()):
    raise Exception("error: user is stupid (x deve ser um número!)")

x = int(x)
l = fib(x)

print(l)

if(x in l):
    print(str(x) + " é um número de Fibonacci!")
else:
    print(str(x) + " não é um número de Fibonacci!")
