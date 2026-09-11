def adicionar_contato(lista, nome_contato):
  contato = {"pessoa": nome_contato, "favorito": False}
  
  lista.append(contato)
  return
def inspecionar_contatos(lista):
  print("\nOs contatos cadastrados foram: \n")
  for i, p in enumerate(lista, start=1):
    status = "⭐" if p["favorito"] else " "
    print(f"{i}. [{status}] {p['pessoa']}\n")
  return
def editar_contato(lista, indice_pessoa, novo_nome):
  indice_ajustado = indice_pessoa - 1
  if indice_ajustado >= 0 and indice_ajustado < len(lista):
    lista[indice_ajustado]['pessoa'] = novo_nome
  else:
    print("Indice invalido!")
    return
def favoritar_contato(lista, indice_contato):
  indice_ajustado = indice_contato - 1
  if indice_ajustado >= 0 and indice_ajustado < len(lista):
    lista[indice_ajustado]['favorito'] = True
  else:
    print("Indice invalido!")
  return
def ver_favoritos(lista):
  print("LISTA DE CONTATOS FAVORITADOS \n")
  contador = 1
  for p in (lista):
    if p['favorito'] == True:
      print(f"{contador}. [⭐] {p['pessoa']}\n")
      contador += 1
  return
def apagar_contato(lista, indice):
  indice_ajustado = indice - 1
  if indice_ajustado >= 0 and indice_ajustado < len(lista):
    for p in lista:
      lista.pop(indice_ajustado)
      print(f"A pessoa selecionada foi removida com sucesso!")
  else:
    print("Nenhuma pessoa foi removida, voce selecionou um indice inexistente!")
  return

contatos = []
while True:
  print("1. Adicionar contato")
  print("2. Ver contatos")
  print("3. Editar contato")
  print("4. Favoritar")
  print("5. Ver favoritos")
  print("6. Apagar contato")
  print("7. Sair")

  opcao = input("Digite um numero para executar alguma acao: ")

  if opcao == "1":
    nome_pessoa = input("Informe o nome da pessoa que deseja cadastrar: ")
    adicionar_contato(contatos, nome_pessoa)
    print(f"{nome_pessoa} cadastrado com sucesso!")
  elif opcao == "2":
    inspecionar_contatos(contatos)
  elif opcao == "3":
    inspecionar_contatos(contatos)
    indice = int(input("Digite o indice da pessoa que deseja alterar o nome: "))
    nome_novo = input("Digite o novo nome que voce ira dar para essa pessoa: ")
    editar_contato(contatos, indice, nome_novo)
  elif opcao == "4":
    inspecionar_contatos(contatos)
    indice = int(input("Digite o indice da pessoa que voce deseja favoritar: "))
    favoritar_contato(contatos, indice)
  elif opcao == "5":
    ver_favoritos(contatos)
  elif opcao == "6":
    inspecionar_contatos(contatos)
    indice = int(input("Digite o indice da pessoa que deseja apagar o contato: "))
    apagar_contato(contatos, indice)
  elif opcao == "7":
    break