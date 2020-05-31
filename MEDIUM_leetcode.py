import collections

#1
"""
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one 
group. Given the array groupSizes of length n telling the group size each person belongs
 to, return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. 
Also, it is guaranteed that there exists at least one solution. 
"""
groupSizes = [3,3,3,3,3,1,3]


def groupThePeople(groupSizes):
    count = collections.defaultdict(list)
    for i, size in enumerate(groupSizes):
        count[size].append(i)
    return [l[i:i + s] for s, l in count.items() for i in range(0, len(l), s)]

print(groupThePeople(groupSizes))


#2
"""
Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
"""

nums = [1,2,3,4]

def decompressRLElist(nums):
    result = []
    for i in range(len(nums)-2):
        result.append(nums[i]) * nums[i+1]
    return result

print(decompressRLElist(nums))
