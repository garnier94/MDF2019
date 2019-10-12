def longest_increasing_subsequence(liste):
    n = len(liste)
    P =[]
    M =[0 for i in range(n+1)]
    L = 0
    for i in range(1, n+1):
        jm = 0
        for j in range(L,0, -1):
            if liste[M[j]] < liste[i-1]:
                jm = j
                break
        P.append(M[jm])
        if jm == L or liste[M[jm+1]]> liste[i-1] :
            M[jm+1] =i-1
            L = max(L,jm+1)
    return L, P

