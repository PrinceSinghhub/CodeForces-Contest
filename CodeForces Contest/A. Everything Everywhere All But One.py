t = int(input())

for i in range(t):

    n = int(input())

    arr = list(map(int,input().split()))

    div = n - 1

    flag = True

    for i in range(n):

        temp = 0

        for j in range(n):
            if i == j:
                continue
            else:
                temp+=arr[j]

        if temp % div == 0 and temp // div == arr[i]:
            print("YES")
            flag = False
            break
    if flag == True:
        print("NO")

'''
4
3
42 42 42
5
1 2 3 4 5
4
4 3 2 1
3
24 2 22

'''