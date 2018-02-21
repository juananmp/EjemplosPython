#Voy a crear un bucle for

lista = ["Juanan","Rodri","Javi","Hec"]

for listas in lista:
	print(listas)

#quiero sacar solo juanan y rodri

limite = 0
indice = 2

print("Esto es un bucle For con limites")
for listas in lista:
	limite +=1
	print(listas)
	if limite == indice:
		break
		
#para ejecutar un script en atom se usa ctrl+shift+b
print("Quiero sacar el tercero y cuarto")
limite2 = lista[2:4]
for listas in limite2:
	print(listas)
