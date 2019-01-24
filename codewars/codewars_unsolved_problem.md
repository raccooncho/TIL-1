simple sum of pairs - 시간 초과

```python
def solve(n):     
    int_list = [[a, b] for a in range(n) for b in range(n) if a + b == n and a >= b]    
    sum_list = []
    for n_list in int_list:
        m = str(n_list[0]) + str(n_list[1])       
        m = sum(map(int, str(m)))
        sum_list.append(m)
    result = max(sum_list)    
    
    return result
```

sum of pairs 

```python
def sum_pairs(ints, s):

    l = len(ints)   

 

    for x in range(l):

            for y in range(l):

                if x < y and ints[x] + ints[y] == s:

                    return [ints[x], ints[y]]

                    

sum_pairs([10, 5, 2, 3, 7, 5], 10)
```

