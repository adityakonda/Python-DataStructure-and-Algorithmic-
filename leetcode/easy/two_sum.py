# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):

    result = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            if i+j == target:
                result.append(i)
                result.append(j)

    return result

def twoSum_1(num, target):
    map = {}
    for i in range(len(num)):
        if num[i] not in map:
            map[target - num[i]] = i + 1
        else:
            return map[num[i]], i + 1

    return -1, -1

print(twoSum_1(num = [8,7,10,2], target= 10))