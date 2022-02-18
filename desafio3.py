def main(palavra):
    contar = 0
    for i in range(0, len(palavra)-1):
        for k in range (1, len(palavra)-i):
            slices1 = palavra[i:i+k]
            for j in range (i+1 , len(palavra)):
                slices2 = palavra[j:j+k]
                if sorted(list(slices2)) == sorted(list(slices1)):
                    contar += 1
                    print(f'({slices1}, {slices2})')

    print(contar)


main(' palavra ')