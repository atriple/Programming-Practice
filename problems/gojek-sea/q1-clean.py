t = int(input())
for i in range(1, t + 1):
    A = int(input())
    B = int(input())
    K = int(input())

    count = 0
    for j in range(A, B+1):
        if (j % K == 0):
            count = count + 1
    
    print("Case {}: {}".format(i, count))