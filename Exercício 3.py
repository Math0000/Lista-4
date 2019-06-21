'''
Esse programa preenche uma matriz binaria de um arquivo txt
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''

print("...................................................................... ")
print("Aqui tu pode brincar de paint do Windows com uma matriz binaria")
print("Digira iniciar() pra iniciar o programa")
print("...................................................................... \n")


#-------------------------------------------------Essa função recursiva espalha os 0 na matriz igual doença-------------------------------------#
def infecção():
    #Aquelas global que eu não queria ficar passando
    global  mat_p, movi, cont, zero_novo, zero_velho, zero_inter

    #Contador rolando sempre que a função for chamada
    cont+=1
    
    for i in zero_inter:
        zero_novo.append(i)
    zero_inter.clear()
    
    for i in zero_novo:#Pega geral do novo e taca como bacteria
        pintar(i)#Manda a bacteria infectar os cara ao redor
        zero_velho.append(i)#Tranforma ela em borda pra não ser mais pintada
        
    zero_novo.clear()#Tira a bacteria usada pra não ficar passando toda hora na pintura
    
    for i in zero_inter:# Pega os cara que a função pintar botou no grupo intermediario e taca nó novo
        zero_novo.append(i)
    zero_inter.clear()
    
    if cont%movi == 0:#Contador rolando pra printar a matriz
        print_mat()
        k = input("Pressione Enter pra continuar")
    
    if len(zero_novo) != 0:#Checa se ainda tem gente pra pintar e chama a rotina de novo
        infecção()
    return
#---------------------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------Essa rotina põe 4 0s em volta do parametro passado a ela-------------------------------------------#
def pintar(bact):
    #As global de novo ai
    global mat_p, n, zero_velho, zero_novo, zero_inter

    #Pinta o cara a direita da bacteria se ele não estiver fora da matriz ou não for borda
    if bact+1 <= len(mat_p)-1 and bact+1 not in zero_velho:
        mat_p[ bact+1 ] = 0
        #Esse cara que foi pintado agora vai pro grupo intermediario se já não tiver nele
        if bact+1 not in zero_inter:
            zero_inter.append(bact+1)
        
    #Pinta o cara a esquerda da bacteria se ele não estiver fora da matriz ou não for borda        
    if bact-1 >= 0 and bact-1 not in zero_velho:
        mat_p[ bact-1 ] = 0
        #Esse cara que foi pintado agora vai pro grupo intermediario se já não tiver nele
        if bact-1 not in zero_inter:
            zero_inter.append(bact-1)

    #Pinta o cara a cima da bacteria se ele não estiver fora da matriz ou não for borda              
    if bact-n >= 0 and bact-n not in zero_velho:
        mat_p[ bact-n ] = 0
        #Esse cara que foi pintado agora vai pro grupo intermediario se já não tiver nele        
        if bact-n not in zero_inter:
            zero_inter.append(bact-n)
            
    #Pinta o cara a baixo da bacteria se ele não estiver fora da matriz ou não for borda 
    if bact + n <= len(mat_p)-1 and bact+n not in zero_velho:
        mat_p[bact+n] = 0
        #Esse cara que foi pintado agora vai pro grupo intermediario se já não tiver nele
        if bact+n not in zero_inter:
            zero_inter.append(bact+n)
 
    return
#-------------------------------------Essa rotina pega a matriz já bonitinha e printa mais bonitinha ainda------------------------------------
def print_mat():    
    global mat_p, m, n

    print()
    for i in range (m):
        for j in range (n):
            print("{0}".format(mat_p[i*n + j]),sep="",end="")
        print()
    print()
    return
#---------------------------------------------------------------------------------------------------------------------------------------------#

#--------------------------------------------Aqui o programa abre a matriz binaria do arquivo txt---------------------------------------------#
def ler_arq(nome):
    try:
        arq = open('{}.txt'.format(nome))
    except FileNotFoundError:
             print("Esse aquivo ai não existe não em, tenta de novo ai")
             nome = str(input("Digita ai o nome do arquivo que esta com a matriz "))
             ler_arq(nome)
             
    paradas = arq.read()
    mat = paradas.split()
    arq.close()
    return mat
#---------------------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------Essa rotina aqui comanda as parada toda---------------------------------------------#

def iniciar():
    #Eu tava com preguiça de ficar passando parametro entre as subrotinas então eu deixei tudo global
    global mat_p, mat, m, n, a, movi, cont, zero_velho, zero_novo, zero_inter

    #Essa parte le o arquivo txt e estrai a matriz
    nome = str(input("Digita ai o nome do arquivo que esta com a matriz "))
    mat = ler_arq(nome)

    #Essa parte pega a matriz que estra como lista de strings e da um split total em tudo, separando cada letra das strings
    mat_p = []
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        for j in range(n):
            #Esse try aqui é porque no meio das strings vai ter um X (indicando onde vai começar o preenchimento)
            #ai já faz o tratamento pra não dar ValueError na conversão e ainda salva o indice dele pra depois
            try:
                mat_p.append(int(mat[i][j]))
            except ValueError :
                mat_p.append(mat[i][j])
                a = i*n+j
    #Printa a matriz do txt antes do preenchimento
    print()
    print("Sua matriz é assim:")
    print()
    for i in range (m):
        print(mat[i])
    print()

    #Define de quantas em quantas etapas de preenchimento a imagem vai ser printada
    try:
        movi = int(input("Após quantos movimentos você quer mostrar o estado da figura? "))
    except ValueError:
        movi = 1
    
    #Cria 3 grupos classificatorios de 0 os que não podem ser pintados (velho), os que vão ser pintados (novo)
    # e um grupo intermediario usado pra passar do velho pro novo sem dar merda ( que eu testei e deu )

    zero_velho = []
    for i in range(len(mat_p)):
        if mat_p[i] == 0:
            zero_velho.append(i)
            
    mat_p[a] = 0
    zero_novo = [a]
    zero_inter = []
    
    #Aqui é pra criar o contador de movimentos e chamar a subrotina recursiva que espalha os 0 na matriz tipo doença
    cont = 0
    infecção()

    print("O preenchimento chegou ao fim, resultado:")
    print_mat()

    return   
#---------------------------------------------------------------------------------------------------------------------------------------------# 















    

