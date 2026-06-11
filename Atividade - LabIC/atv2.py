def somaArray(array):
    soma = 0
    for x in array:
        soma += x
    soma_strg = " + ".join(str(x) for x in array)
    print(f"{soma_strg} = {soma}")
    

n = int(input()) #mantive pq estava no enunciado, mas como usei list cc
array = [int(x) for x in input().split()]
somaArray(array)
