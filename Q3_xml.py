import xmltodict #é necessário instalar o módulo

file = open("dados(2).xml", "r").read()

file = "<doc>\n" + file + "\n</doc>"

data = xmltodict.parse(file)

data = data['doc']['row']

newdata = []
for e in data:
    if not float(e['valor']) == 0.0:
        newdata.append(e)

data_valor = [float(e['valor']) for e in newdata]

print(str(min(data_valor)) + " é o menor valor de faturamento ocorrido no mês")

print(str(max(data_valor)) + " é o maior valor de faturamento ocorrido no mês")

m = sum(data_valor)/len(data_valor)
n = 0
for e in data_valor:
    if(e > m):
        n += 1

print(str(n) + " é o número de dias do mês em que o faturamento mensal é maior que a média")
