nome_title = 'Nome'
cod_title = 'Codigo'
fat_title = 'Faturamento'
quantd = 'Quantidade'
def naoprocas():
    print('Não existe produto cadastrado!!')
def opcinvalid():
    print('ERRO, Valor inválido')
def menu():
    opc = int(input('''
Digite a OPÇÃO desejada :
1 - Cadastrar PRODUTO 
2 - Consultar PRODUTO 
3 - Consultar ESTOQUE  
4 - Registrar VENDA
5 - Relatório de VENDA
6 - Inserir PRODUTO no ESTOQUE
7 - Remover PRODUTO do ESTOQUE
8 - Para sair            \n'''))
    return opc
def titleestoque():
    print(f'\nESTOQUE ATUALIZADO')
    print(f'{nome_title.ljust(15)} {cod_title.center(15)} {quantd.rjust(15)}\n')
def titlefat():
    print(f'\nRelátorio de VENDAS')
    print(f'\n{nome_title.ljust(15)} {cod_title.center(15)} {fat_title.rjust(15)}\n')
