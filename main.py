from database import produtos, categorias
from lib import funcoes

while True:

    print("""
            Escolha uma opção
    1 - Gerenciar Categorias 
    2 - Gerenciar Produtos
         """) 
    menu = int(input('Oque temos para hoje: '))
    if type(menu) == str:
        print('Apenas numeros de 1 a 2')
    
    
    if menu == 1:
        while True:
            print("""
                        Categorias
                1 - Criar categorias
                2 - Listas das Categorias 
                3 - Consultar Categorias
                4 - Atualizar Categorias
                5 - Deletar Categorias
                6 - Voltar
                """
            )
            menu2 = int(input('Oque temos para hoje: '))
            if menu2 == 1:
                funcoes.criar_categorias(categorias)
                menu2
            elif menu2 == 2:
                funcoes.exibir_categorias(categorias)
                menu = 1
            elif menu2 == 3:
                funcoes.consultar_categorias(categorias, produtos)
                menu2
            elif menu2 == 4:
                funcoes.atualizar_categorias(categorias)
                menu2
            elif menu2 == 5:
                funcoes.deletar_categorias(categorias)
                menu2
            elif menu2 == 6:
                break
        
                
        
        
    if menu == 2:
        while True:
            print("""
                        Produtos
                1 - Criar Produtos
                2 - Listas dos Produtos 
                3 - Atualizar Produtos
                4 - Deletar Produtos
                5 - Voltar
                """
            )
            menu3 = int(input('Oque temos para hoje: '))
            if menu3 == 1:
                funcoes.criar_produto(produtos)
            elif menu3 == 2:
                funcoes.exibir_produto(produtos)
            elif menu3 == 3: 
                funcoes.atualizar_produto(produtos)
            elif menu3 == 4: 
                funcoes.deletar_produto(produtos)
            elif menu3 == 5:
                break
    else:
        print('Valor Invalido.')