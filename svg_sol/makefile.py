name = input().rstrip('\n')
N = int(input())

dict_tt = dict()
for i in range(N):
    a = input().split(' ')
    M = int(a[1])
    pere = a[0]
    for i in input().rstrip('\n').split(' '):
        if not i in dict_tt.keys():
            dict_tt[i] = [pere]
        else:
            if not pere in dict_tt[i]:
                dict_tt[i] += [pere]
a = list()
a_old = [name]
while len(a_old) != 0:
    ol = a_old
    a_old =[]
    for old in ol:
        if old in dict_tt.keys():
            for i in dict_tt[old]:
                if not i in a:
                    a_old.append(i)
                    a.append(i)


print(len(a))
for i in a:
    print(i)