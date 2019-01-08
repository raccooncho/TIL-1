```python
# 달력 만들기
for month in range(1, 13):
    print(f'{month}월')
    print('일 월 화 수 목 금 토')
    print('-' * 19)
    for i in range(1, 7):
        for j in range(1,8):
            day = str((i - 1) * 7 + j)
            print(day, end ='  ') if len(day) == 1\
            else print(day, end =' ')
            if month in [1, 3, 5, 7, 8, 10, 12] and day == '31':
                break
            elif month in [4, 6, 9, 11] and day == '30':
                break
            elif month == 2 and day == '28':
                break
        print()
        if month in [1, 3, 5, 7, 8, 10, 12] and day == '31':
            break
        elif month in [4, 6, 9, 11] and day == '30':
            break
        elif month == 2 and day == '28':
            break
    print()
```

