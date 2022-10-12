#mensagem inicial
print('                  \033[36mRESTAURANTE GULA-GULA!\033[m')
print('\n             \033[36m*REFEIÇÕES, PETISCOS E BEBIDAS*\n\033[m')

#CARDAPIO
ITENS = {
 1: 'SALADA VERDE',
 2: 'MACARRÃO', 
 3: 'VATAPÁ',
 4: 'BATATA FRITA',
 5: 'CASILLERO DEL DIABLO',
 6: 'BIFÃO TRADICIONAL',
 7: 'ESTROGONOFE DE CARNE',
 8: 'LINGUIÇA TOSCANA',
 9: 'SOBRECOXA DE FRANGO',
 10: 'LASANHA A BOLONHESA',
 11: 'JACK DANIELS-WHISKEY',
 12: 'PEITO DE FRANGO',
 13: 'SKOL',
 14: 'SMIRNOFF',
 15: 'ÁGUA MINERAL',
 16: 'PICADINHO DO CHEF',
 17: 'BAIÃO CREMOSO',
 18: 'ARROZ BRANCO',
 19: 'FEIJÃO',
 20: 'FEIJOADA',
 21: 'PEPSI',
 22: 'COCA-COLA',
 23: 'GUARANÀ',
 24: 'CAJUÍNA',
 25: 'PICANHA DO CHEFE',


 }

PREÇO = {
1: 3.50, 
2: 3.50, 
3: 2.50, 
4: 4.20, 
5: 12.00, 
6: 4.00, 
7: 4.50, 
8: 3.10, 
9: 3.10, 
10: 5.00, 
11: 120.00, 
12: 2.10, 
13: 3.20, 
14: 15.00, 
15: 3.00, 
16: 5.00, 
17: 4.50, 
18: 4.00, 
19: 3.00, 
20: 7.50, 
21: 7.00, 
22: 7.00, 
23: 7.00, 
24: 7.50, 
25: 8.00

}

PEDIDO = {
1:0, 
2:0, 
3:0, 
4:0, 
5:0, 
6:0, 
7:0, 
8:0, 
9:0, 
10:0, 
11:0, 
12:0, 
13:0, 
14:0, 
15:0, 
16:0, 
17:0, 
18:0, 
19:0, 
20:0, 
21:0, 
22:0, 
23:0, 
24:0, 
25:0

}

#mostrar cardapio
def cardapio():
  for i in range(1, 26):
    print('\033[36m{} - {}\033[m \033[32mR$: {:.2f}\033[m'.format(i, ITENS[i], PREÇO[i]))

#adicionar itens ao pedido
def adicionar():
  for i in range(1, 26):
    print('\033[33m{} - {}\033[m \033[32mR$: {:.2f}\033[m'.format(i, ITENS[i], PREÇO[i]))
  print('\n\033[33mINFORME O ITEM: \033[m')
  pratos = int(input())
  quantidade = int(input('\n\033[92mQUANTAS\033[m \033[4;92m{}\033[m \033[32m(\033[32mR${:.2f}/unidade(s))\033[m\033[m\033[36m?\033[m\n'.format(ITENS[pratos],PREÇO[pratos])))
  PEDIDO[pratos]+=quantidade
  print('\033[32m\nADICIONADO!\033[m')
  return PEDIDO

#excluir itens ao pedido
def excluir():
  for i in range(1, 26):
    print('\033[31m{} - {}\033[m \033[32mR$: {:.2f}\033[m'.format(i, ITENS[i], PREÇO[i]))
  pratos = int(input('\n\033[31mQUAL ITEM DESEJA EXCLUIR?\n\033[m'))
  quantidade = int(input('\n\033[31mQUANTOS {} DESEJA EXCLUIR?\033[m\n'.format(ITENS[pratos])))
  PEDIDO[pratos]-=quantidade
  print('\033[31m\nEXCLUIDO!\033[m')

#visualisar pedido
def pedido():
  print('\033[35m\nPEDIDO:\n\033[m')
  for i in range(1, 26):
    if PEDIDO[i]!=0:
      print('\033[35m{} {}/unidade(s) \033[m(\033[32mR$: {:.2f}) = {:.2f}\033[m'.format(PEDIDO[i], ITENS[i], PREÇO[i], PEDIDO[i]*PREÇO[i]))


#funções e comandos
cardapio() 
mesa=int(input('\n\033[36mQUAL O NUMERO DA MESA?\033[m\n'))
program=1
while program != 0:
  função=int(input('\033[34mINSIRA A OPÇÃO:\n\n\033[36m1 - CARDÁPIO\033[m\n\033[32m2 - ADICIONAR ITENS\033[m\n\033[31m3 - EXCLUIR ITENS\033[m\n\033[35m4 - VISUALIZAR PEDIDO\033[m\n\033[32m5 - PEDIR A CONTA\033[m\n\n'))
  if função==1:
    cardapio()
    print()     
  elif função==2:
    adicionar()
    print()
  elif função==3:
    excluir()
    print()
  elif função==4:
    pedido()
    print()
  elif função==5:
    CONTA=0
    for i in range(1, 26):
      if PEDIDO[i]!=0:
        CONTA+=PEDIDO[i]*PREÇO[i]
        print('\n\033[36m{} {}/unidade(s) \033[m\033[32m(R$: {:.2f}) = {:.2f}\033[m'.format(PEDIDO[i], ITENS[i], PREÇO[i], PEDIDO[i]*PREÇO[i]))
    print('\033[36mCONTA TOTAL: \033[m\033[32mR$ {:.2f}\033[m'.format(CONTA))
    print('\033[36mMESA: {}\033[m'.format(mesa))
    print('\n\033[36mSEU PEDIDO ESTÁ A CAMINHO!!')
    program=0
    print('\n\033[31m!!!FIM DO PROGRAMA!!!\033[m')
    print()
  elif função > 5:
    print('\033[31mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX !!!ESSA FUNÇÃO NÃO EXISTE!!! XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\033[m')
    print('\033[31mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\033[m')
    print('\033[31mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX !!!ESCOLHA A OPÇÃO VÁLIDA!!! XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\033[m')
  elif função <= 0:
    print('\033[31mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX !!!ESSA FUNÇÃO NÃO EXISTE!!! XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\033[m')
    print('\033[31mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\033[m')
    print('\033[31mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX !!!ESCOLHA A OPÇÃO VÁLIDA!!! XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\033[m')