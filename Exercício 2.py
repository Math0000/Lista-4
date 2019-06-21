'''
Esse programa resolve a torre de Hanói com n discos
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''

print("...................................................................... ")
print("Aqui você pode escolher com quantos discos a torre de Hanoi será")
print("resolvida e também pode ver o passo a passo")
print("...................................................................... \n")

#----------------------------------------------Essa função aqui printa como a torre ta durante o processo-----------------------------------------#
def mostrar(m):

    print("Após {} movimentos os discos estão nas posições:".format(m))# fala o numero de movimentos feitos até agora
    
    for i in range (n+1,-1,-1):#Bagulho boladão pra printar a torre bonitninha, com varios tratamento de exceção
                               #porque as vezes o algoritmo tentava consultar um indice da lista que não existia
        try:#Pra torre 1
            print(" "*(4+n-p1[i]),"#"*p1[i],"|","#"*p1[i]," "*(2+n-p1[i]),sep="", end="")
        except IndexError :
            print(" "*(4+n),"|"," "*(2+n),sep="", end="")
            
        try:#Pra torre 2
            print(" "*(2+n-p2[i]),"#"*p2[i],"|","#"*p2[i]," "*(2+n-p2[i]),sep="", end="")
        except IndexError :
            print(" "*(2+n),"|"," "*(2+n),sep="", end="")
            
        try:#Pra torre 3
            print(" "*(2+n-p3[i]),"#"*p3[i],"|","#"*p3[i]," "*(4+n-p3[i]),sep="")
        except IndexError :
            print(" "*(2+n),"|"," "*(4+n),sep="")
    print("-"*(19+n*6),sep="")
    return

#-------------------------------------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------------Essa função é a que faz a porra toda--------------------------------------------------------#
def move_1(origem, destino):
    global cont, m
    cont += 1# contador de movimentos feitos
    destino.append(origem.pop())
    if cont%m == 0:# Esquema pra printar a torre quando forem feitos o numero de movimentos escolhido pelo usuario
        mostrar(cont)
        k=input("Precione Enter para continuar")#Prosegue pro proximo só se ele apertar enter
        print()
    return
#-------------------------------------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------Pega o que faz a porra toda e manipula ela--------------------------------------------------------#
def move_n(n, origem, inter, destino):
    if n>1:
        move_n(n-1,origem,destino, inter)
        move_1(origem, destino)
        move_n(n-1, inter, origem, destino)
    else:
        move_1(origem, destino)

    return
#-------------------------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------Daqui pra baixo guia os parametros do programa e define coisas--------------------------------------------#

#Define o numero de discos e numero de movimentos
try:#Botei só pra ter um minimo de discos
    n = int(input("Fala o numero de discos que serão usados ai "))
except  ValueError :
    print("O numero de discos precisa ser um inteiro meu filho")
    print("O sistema vai considerar o padrão de 3 discos pra essa sessão")
    n = 3

try:#Esse aqui só pra ter um minimo de movimentos pra mostrar
    m = int(input("Após quantos movimentos deve-se mostrar as pilhas de discos? "))
except  ValueError :
    print("Esse valor precisa ser um numero inteirobrother")
    print("O sistema vai considerar o padrão de mostrar a cada 1 movimento")
    m = 1
    
#Minhas pilhas
p1 = list(range(n,0,-1))
p2 = []
p3 = []
cont = 0

#Print de como a torre ta inicialmente
print()
print("Inicialmente as torres estão assim:")
for i in range (n+1,-1,-1):
    try:
        print(" "*(4+n-p1[i]),"#"*p1[i],"|","#"*p1[i]," "*(2+n-p1[i]),sep="", end="")
    except IndexError :
        print(" "*(4+n),"|"," "*(2+n),sep="", end="")
    try:
        print(" "*(2+n-p2[i]),"#"*p2[i],"|","#"*p2[i]," "*(2+n-p2[i]),sep="", end="")
    except IndexError :
        print(" "*(2+n),"|"," "*(2+n),sep="", end="")
    try:
        print(" "*(2+n-p3[i]),"#"*p3[i],"|","#"*p3[i]," "*(4+n-p3[i]),sep="")
    except IndexError :
        print(" "*(2+n),"|"," "*(4+n),sep="")
print("-"*(19+n*6),sep="")

#chamando a função pra fazer tudo
move_n(n,p1,p2,p3)

#Print de como a torre termina
print("A torre foi resolvida em {} movimentos".format(cont))
for i in range (n+1,-1,-1):
    try:
        print(" "*(4+n-p1[i]),"#"*p1[i],"|","#"*p1[i]," "*(2+n-p1[i]),sep="", end="")
    except IndexError :
        print(" "*(4+n),"|"," "*(2+n),sep="", end="")
    try:
        print(" "*(2+n-p2[i]),"#"*p2[i],"|","#"*p2[i]," "*(2+n-p2[i]),sep="", end="")
    except IndexError :
        print(" "*(2+n),"|"," "*(2+n),sep="", end="")
    try:
        print(" "*(2+n-p3[i]),"#"*p3[i],"|","#"*p3[i]," "*(4+n-p3[i]),sep="")
    except IndexError :
        print(" "*(2+n),"|"," "*(4+n),sep="")
print("-"*(19+n*6),sep="")
