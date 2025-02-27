inventario=[]
resposta = "S"

# #adicionar item no inventario
# while resposta == "S":
#     equipamento = [
#         input("Equipamento: "),
#         float(input("Valor: ")),
#         int(input("Número Serial: ")),
#         input("Departamento: ")
#     ]
#     inventario.append(equipamento)  
#     resposta = input('Digite "S" para continuar: ').upper()  

# #localizar um item no inventario
# busca = input("Digite o nome do equipamento que deseja buscar: ")
# for elemento in inventario:
#   if busca==elemento[0]:
#     print("Valor..: ", elemento[1])
#     print("Serial.:", elemento[2])

# #depreciar itens no inventario
# depreciacao = input("Digite o nome do equipamento que será depreciado: ")
# for elemento in inventario:
#     if depreciacao == elemento[0]:  # Verifica se o nome do equipamento corresponde
#         print("Valor antigo: ", elemento[1])  # Exibe o valor antigo
#         elemento[1] = elemento[1] * 0.9  # Aplica a depreciação de 10%
#         print("Novo valor: ", elemento[1])  # Exibe o novo valor
#         break  # Sai do loop após encontrar e depreciar o equipamento

# #excluir um item do inventario
# serial=int(input("Digite o serial do equipamento que será excluído: "))
# for elemento in inventario:
#   if elemento[2]==serial:
#     inventario.remove(elemento)

# #exibir dados do inventário
# for elemento in inventario:
#   print("Nome.........: ", elemento[0])
#   print("Valor........: ", elemento[1])
#   print("Serial.......: ", elemento[2])
#   print("Departamento.: ", elemento[3])


def preencherInventario(lista):
  resp="S"
  while resp == "S":
    equipamento=[input("Equipamento: "),
              float(input("Valor: ")),
              int(input("Número Serial: ")),
              input("Departamento: ")]
    lista.append(equipamento)
    resp = input("Digite S para continuar: ").upper()

def exibir_inventario(lista):
  for elemento in lista:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

def localizarPorNome(lista):
  busca=input("Digite o nome do equipamento que deseja buscar: ")
  for elemento in lista:
    if busca==elemento[0]:
      print("Valor..: ", elemento[1])
      print("Serial.:", elemento[2])

def depreciarPorNome(lista, porc):
  depreciacao=input("Digite o nome do equipamento que será depreciado: ")
  for elemento in lista:
    if depreciacao==elemento[0]:
      print("Valor antigo: ", elemento[1])
      elemento[1] = elemento[1] * (1-porc/100)
      print("Novo valor: ", elemento[1])
    
def excluirPorSerial(lista):
  serial=int(input("Digite o serial do equipamento que será excluido: "))
  for elemento in lista:
    if elemento[2]==serial:
      lista.remove(elemento)
  return "Itens excluídos."    

def resumirValores(lista):
  valores=[]
  for elemento in lista:
    valores.append(elemento[1])
  if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))
