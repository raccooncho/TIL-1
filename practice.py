def pair_sum(nums, target):
    result = [ [nums.index(a), nums.index(b)] for a in nums for b in nums if a + b == target and a != b ] 
    if result == []:
        return None
    return result[0]

print(pair_sum([4, 2, 8, 9, 6], 123123))