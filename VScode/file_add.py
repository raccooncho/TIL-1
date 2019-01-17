f = open("새파일.txt", 'a')
for i in range(11, 20):
    data = f'this is additional line {i}'
    f.write(data)
f.close
