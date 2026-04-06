lista_de_compras = []

def verificar_comando():
    while True:
        comando = input('''
 digite uma opção:                                                       
(1) adicionar
(2) excluir 
(3) finalizar                       
 '▶️ ▶️ ▶️ ▶️' :''')
        
        if comando == '1':
            return adicionar_valor()
        
        elif comando == '2':
              excluir_valor_da_lista()

        elif comando == '3':
              exibir_lista()
              break
                           
        else:
            print('comando invalido 😔😔')
            return verificar_comando()


def exibir_lista():
        print('--- qt    --- item')
        for iten, lista in enumerate(lista_de_compras, start=1):
            print('✅',iten, lista)

def adicionar_valor():
                adiconar_valor_a_lista = input('adicione itens a lista: ')
                lista_de_compras.append(adiconar_valor_a_lista)
                exibir_lista()
                verificar_comando()

def excluir_valor_da_lista():
      lista_de_compras.pop()
      verificar_comando()

verificar_comando()
