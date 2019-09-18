##MDF 2017

def parcours_table(table, N):
    i,j = 0,0

    set =[]
    if table[0][0] == 'X':
        set += [[0,0]]


    while i !=N-1 or j !=N-1:
        ec =-1
        for k in range(j+1,N):
            if table[i][k] =='X':
                ec = k
                set += [[i,k]]
                break

        if ec == -1:
            if i == N-1:
                i,j =N-1,N-1
            else:
                if table[i+1][j] == 'X':
                    set += [[i+1, j]]
                i,j = i+1,j
        else:
            i,j =i,k
    return set



def main():

    # Lecture de Table
    N = int(input())
    table = list()
    for i in range(N):
        table.append(list(input()))

    re = sum(sum(table[i][j] == 'X' for i in range(N))for j in range(N))

    ct = 0
    while  re !=0 and ct < N:
        ct +=1
        ret = parcours_table(table, N)
        #print(ret)
        for elem in ret:
            table[elem[0]][elem[1]] = 'o'
        re = sum(sum(table[i][j] == 'X' for i in range(N)) for j in range(N))


    print(ct)