fat = {"SP" : 67836.43, "RJ" : 36678.66, "MG" : 29229.88, "ES": 27165.48, "Outros": 19849.53} #faturamento dos estados

fat_tot = sum(fat.values()) #faturamento total

porc = {est : str(round(100*fat[est]/fat_tot,2))+"%" for est in fat.keys()} #dicionário com as porcentagens de cada estado (aproximadas)

print(porc)