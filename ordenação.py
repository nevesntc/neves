from ast import Or
import random
import time
class Ordenação:
    listabobble = []
    listaselection = []
    listainsertion = []

    def bobblesort(A):
       Ordenação.listabobble = A
       n = len(A)
       for i in range(n):
          for j in range (0,len(A)-1):  
            if (A[j]>A[j+1]):
                temp = A[j]  
                A[j] = A[j+1]  
                A[j+1] = temp
            print('Executando...')

    def insertionsort(A):
        Ordenação.listainsertion = A
        n = len(A)
        for j in range(1, n):
           chave = A[j]
           i = j - 1

        while i >= 0 and A[i] > chave:
            A[i + 1] = A[i]
            i = i - 1
            A[i + 1] = chave
        print('Executando...')

    def selectionsort(A):
        Ordenação.listaselection = A
        n = len(A)
        for i in range(n):
            minimo = i
            for j in range(i + 1, n):
                if A[j] < A[minimo]:
                    minimo = j
            A[i], A[minimo] = A[minimo], A[i]
        print('Executando...')

    def menu():

        print('*****************************')
        print('**\033[1;1m Algoritmos de Ordenação **')
        print('*****************************')
        print('')
        print('')
        print('1 - Selection Sort') 
        print('2 - Insertion Sort')
        print('3 - Bobble Sort')
        print('4 - Sair')

        c = int(input(''))

        if c == 1:
            Ordenação.selectionsortmenu()
        
        elif c == 2:
            Ordenação.insertionsortmenu()

        elif c == 3:
            Ordenação.bobblesortmenu()
        
        elif c == 4:
            exit()
   
    def selectionsortmenu():
        print('********************')
        print('** Selection Sort **')
        print('********************')
        print('')
        print('')
        print('1 - Gerar lista valores') 
        print('2 - Executar algoritmo')
        print('3 - Listar conteúdo')
        print('4 - Voltar para o menu anterior')

        c = int(input(''))

        if c == 1:
            Ordenação.selectionsortgerar()
        
        elif c == 2:
            Ordenação.selectionsortexec()

        elif c == 3:
            Ordenação.selectionsortlist()
        
        elif c == 4:
            Ordenação.menu()

    def insertionsortmenu():
        print('********************')
        print('** Insertion Sort **')
        print('********************')
        print('')
        print('')
        print('1 - Gerar lista valores') 
        print('2 - Executar algoritmo')
        print('3 - Listar conteúdo')
        print('4 - Voltar para o menu anterior')

        d = int(input(''))

        if d == 1:
            Ordenação.insertionsortgerar()
        
        elif d == 2:
            Ordenação.insertionsortexec()

        elif d == 3:
            Ordenação.insertionsortlist()
        
        elif d == 4:
            Ordenação.menu()

    def bobblesortmenu():
        print('********************')
        print('** Bobble Sort **')
        print('********************')
        print('')
        print('')
        print('1 - Gerar lista valores') 
        print('2 - Executar algoritmo')
        print('3 - Listar conteúdo')
        print('4 - Voltar para o menu anterior')

        b = int(input(''))

        if b == 1:
            Ordenação.bobblesortgerar()
        
        elif b == 2:
            Ordenação.bobblesortexec()

        elif b == 3:
            Ordenação.bobblesortlist()
        
        elif b == 4:
            Ordenação.menu()
    
    def selectionsortgerar():

        o = int(input('Escolha a quantidade de valores aleatórios a serem gerados --->  '))
        
        Ordenação.listaselection = random.sample(range(0,1000), o)
        time.sleep(2)
        Ordenação.selectionsortmenu()

    def selectionsortexec():
        Ordenação.selectionsort(Ordenação.listaselection)
        time.sleep(2)
        Ordenação.selectionsortmenu()
    
    def selectionsortlist():
        print(Ordenação.listaselection)
        print('')
        print('')
        print('Para voltar ao menu, pressione "Enter"')

        user_input = input('')

        if user_input == '':
            Ordenação.selectionsortmenu()
        else:
            Ordenação.selectionsortmenu()

    def insertionsortgerar():

        o = int(input('Escolha a quantidade de valores aleatórios a serem gerados --->  '))
        
        Ordenação.listainsertion = random.sample(range(0,1000), o)
        time.sleep(2)
        Ordenação.insertionsortmenu()

    def insertionsortexec():
        Ordenação.insertionsort(Ordenação.listainsertion)
        time.sleep(2)
        Ordenação.insertionsortmenu()

    def insertionsortlist():
        print(Ordenação.listainsertion)
        print('')
        print('')
        print('Para voltar ao menu, pressione "Enter"')

        user_input = input('')

        if user_input == '':
            Ordenação.insertionsortmenu()
        else:
            print('Pressione "Enter" para voltar ao menu')

    def bobblesortgerar():

        o = int(input('Escolha a quantidade de valores aleatórios a serem gerados --->  '))
        
        Ordenação.listabobble = random.sample(range(0,1000), o)
        time.sleep(2)
        Ordenação.bobblesortmenu()

    def bobblesortexec():
        Ordenação.bobblesort(Ordenação.listabobble)
        time.sleep(2)
        Ordenação.bobblesortmenu()

    def bobblesortlist():
        print(Ordenação.listabobble)
        print('')
        print('')
        print('Para voltar ao menu, pressione "Enter"')

        user_input = input('')

        if user_input == '':
            Ordenação.bobblesortmenu()
        else:
            print('Pressione "Enter" para voltar ao menu')
Ordenação.menu()

    

    



















    



    

    
