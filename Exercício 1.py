'''
Esse programa le matrizes de aquivos txt
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''

print("...................................................................... ")
print("Aqui tu pode printar uma matriz existente em um arquivo txt")
print("Digira iniciar() pra iniciar o programa")
print("...................................................................... \n")

#Minhas global ta tudo aqui
mat_p = []
mat = []
m = 0
n = 0

#-------------------------------------Essa rotina pega a matriz já bonitinha e printa mais bonitinha ainda------------------------------------#

def printar_matriz():
    
    global mat, m, n
    print("Sua matriz é \n")
    print()
    print("+-"," "*(7*n-2),"-+")
    for i in range (m):
        print("| ",end="")
        for j in range (n):
            print(" {0:^5} ".format((mat[i][j])),end="")

        print(" |")
    print("+-"," "*(7*n-2),"-+")
    return
#---------------------------------------------------------------------------------------------------------------------------------------------#

#---------Essa parte aqui monta a matriz como lista de listas e verifica se o m e o n estão de acordo com os elementos do arquivo-------------#

def montar_matriz():
    global m, n, mat_p, mat
    
    try:
        
        for i in range(m):
            lin = mat_p[2+i*n]
    except IndexError:
        print("O numero de linhas informado no arquivo não ta certo")
        print("Escreve la o que falta no arquivo e depois executa o programa de novo ")
        return 0
    
    try:
        for i in range(m):
            for j in range(n):
                col = mat_p[2 + i*m + j]
    except IndexError:
        print("O numero de colunas informado no arquivo não ta certo")
        print("Escreve la o que falta no arquivo e depois executa o programa de novo")
        return 0
    
    for i in range(m):
        linha = []
        for j in range(n):
            try:
                num = float(mat_p[2 + i*m + j])
            except ValueError:
                print("O maluco na linha {}, coluna {} não é um numero em".format(i+1,j+1))
                num = 'NaN'
            linha.append(num)
        mat.append(linha)
    return 1

#---------------------------------------------------------------------------------------------------------------------------------------------#

#------------Aqui nós lemos o arquivo txt com a matriz e verifica se o numero de linhas e colunas tão escritos e se são numeros---------------#

def ler_arq(nome):
    global mat_p , m, n
    try:
        arq = open('{}.txt'.format(nome))
    except FileNotFoundError:
             print("Esse aquivo ai não existe não em, tenta de novo ai")
             nome = str(input("Digita ai o nome do arquivo que esta com a matriz "))
             ler_arq(nome)
             
    paradas = arq.read()
    mat_p = paradas.split()
    arq.close()
    try:
        m = int(mat_p[0])
        n = int(mat_p[1])
    except IndexError:
        print("O numero de linhas ou de colunas não foi informado no arquivo")
        print("Escreve la o que falta no arquivo e depois executa o programa de novo")
        return 0
    except ValueError:
        print("O que deveria ser o numero de linhas ou colunas não é nem numero")
        print("Escreve la o que falta no arquivo e depois executa o programa de novo")
        return 0
    
    print("A sua matriz é do tipo {}x{}".format(m,n))
    return 1

#---------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------Essa rotina guia as decisões do programa de acordo com as merda que da----------------------------------#

def iniciar():
    nome = str(input("Digita ai o nome do arquivo que esta com a matriz "))
    p1 = ler_arq(nome)

    #Essa parada testa o valor retornado pelo Ler_arq, se for 0 é porque deu merda, se for 1 ta suave e segue o jogo
    if p1 == 0:
        return
    else:
        p2 = montar_matriz()

        #Mesmo esquema do de cima
        if p2 == 0:
            return
        else:
            
            # pra terminar tudo
            printar_matriz()
        return



