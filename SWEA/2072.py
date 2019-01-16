l = input().split(' ')
for i in range(int(l[0])):
    print(f'#{i+1}', end=' ')   
    result = 0
    for k in l[i*10 + 1: (i+1)*10+1]:        
        if int(k) % 2 == 1:
            result += int(k)
    print(result)
