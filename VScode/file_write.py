f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = f'This is line {i}.\n'
    f.write(data)
f.close()