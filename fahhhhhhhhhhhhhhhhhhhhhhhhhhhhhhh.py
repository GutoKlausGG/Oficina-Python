compras = []
item = input("Item (fim para parar):")
while item != "fim":
    compras.append(item)
    item = input("Item (fim para parar):")
print ("Sua lista:", compras)
print("Total de itens", len(compras))