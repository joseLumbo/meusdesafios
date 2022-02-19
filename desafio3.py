
#Esta função encontra os numeros de anagramas na posição para
def main(word):
    contar = 0
    for i in range(0, len(word)-1):
        for k in range (1, len(word)-i):
            word_part1 = word[i:i+k]
            for j in range (i+1 , len(word)):
                word_part2 = word[j:j+k]
                if sorted(list(word_part2)) == sorted(list(word_part1)):
                    contar += 1
                    print(f'({word_part1}, {word_part2})')

    print(contar)

#Chamando a função main
main(' word ')
