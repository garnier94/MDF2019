
def rotation(mat, N):
    new_mat = [[0 for i in range(N)] for j in range(N)]
    for i in range(N // 2):
        for  j in range(i, N - i -1):


            new_mat[i][j] =mat[j][N-1-i]
            new_mat[j][N-1-i] =mat[N-1-i][N-1-j]
            new_mat[N-1-i][N-1-j] = mat[N-1-j][i]
            new_mat[N-1-j][i] = mat[i][j]

    return new_mat