
#Criando função para imprimir o número de degraus
def escada(n):
    #Iterando sobre o numero de degraus
    for k in range(1, n + 1):
        for i in range(n, k, -1):
            #Imprimindo o espassamento
            print("", end = " ")
        for z in range(0, k):
            #Imprimindo o asteristico em função a quantidade no range
            print("*", end = '')
        print()

escada(10)
