def criar_categorias(categorias):
    id = len(categorias) +1
    nome = input('Qual o nome da categoria: ')

    categoria = {"id": id, "nome": nome} 
    categorias.append(categoria)
    print(f'A Categoria {nome} foi criada.')

def exibir_categorias(categorias):
    for categoria in categorias:
        id = categoria["id"]
        nome = categoria["nome"]
        print(f'id: {id}, nome: {nome}')
        
def consultar_categorias(categorias, produtos):
    id_categoria = int(input('Digite o id da categoria: '))
    
    categoria_encontrada = None
    for categoria in categorias:
        if categoria["id"] == id_categoria:
            categoria_encontrada = categoria
            print(f"{categoria}")
            break

    if categoria_encontrada:
        nome = categoria_encontrada["nome"]
        print(f"{nome}")
        produtos_categoria = [produto["nome"] for produto in produtos if produto["categoria_id"] == id_categoria]
        if produtos_categoria:
            print(f"Produtos da categoria {nome}:")
            for produto in produtos_categoria:
                print(f" {produto}")
        else:
            print(f"A categoria {nome} não possui produtos.")
    else:
        print("Categoria não encontrada.")
def atualizar_categorias(categorias):
    id = int(input('Qual o id da categoria: '))
    nome = input('Qual o novo nome da categoria: ')
    for categoria in categorias:
        if categoria["id"] == id:
            categoria["nome"] = nome
    print(f'A Categoria foi renomeada para {nome}')

def deletar_categorias(categorias):
    delete = int(input('Qual o id da despesa que deseja excluir: '))
    for categoria in categorias:
        if categoria["id"] == delete:
            indice = delete -1
            del categorias[indice]
    print('A Categoria foi excluida')
    
def criar_produto(produtos):
    id = len(produtos) +1
    nome = input('Qual o nome do produto: ')
    valor = int(input('Digite o preço do produto: '))
    categoria = int(input('Qual o id da categoria: '))

    produto = {"id": id, "Nome": nome, "Categoria": categoria, "Preço": valor}
    produtos.append(produto)
    print(f'O Prudoto {nome} foi criada')

def exibir_produto(produtos):  
    for produto in produtos:
        id = produto["id"]
        nome = produto["nome"]
        valor = produto["valor"]
        categoria = produto["categoria_id"]
        print(f'id: {id}, nome: {nome}, Categoria: {categoria}, Preço: {valor}')

def atualizar_produto(produtos):
    id = int(input('Qual o id do Produto: '))
    nome = input('Qual o novo nome da Produto: ')
    categoria = int(input('Qual o id da nova categoria'))
    valor = int(input('Qual o novo valor do Produto: '))
    for produto in produtos:
        if produto["id"] == id:
            produto["nome"] = nome
            produto["categoria"] = categoria
            produto["valor"] = valor
    print(f'O produto {nome} foi editado')
    
def deletar_produto(produtos):
    delete = int(input('Qual o id do Produto'))
    for produto in produtos:
        if produto["id"] == delete:
            indice = delete -1 
            del produtos[indice]
        print("O produto foi excluido")
        
