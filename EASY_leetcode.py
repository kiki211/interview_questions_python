
# Return only even(2,4,6 etc) length of digits, how many in the list.
nums = [12,345,2,6,7896]
def findNumbers(nums):
    counter = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            counter += 1
    return counter

print(findNumbers(nums))

"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", 
each substring contains same number of 'L' and 'R'.
"""
# Balanced string
def balancedStringSplit(s):
    count, temp = 0, 0
    for val in s:
        if val == "R":
            count += 1
        else:
            count -= 1
        if count == 0:
            temp += 1
    return temp

# return string all in lower case
str = "HeLlo"
def toLowerCase(str) -> str:
    return "".join(l.lower() for l in str)

print(toLowerCase(str))

"""
How many steps needed to get num to 0 
by dividing it by 2 or substr 1 if num is odd
"""
num = 14  # answer 6
def numberOfSteps(num) -> int:
    count = 0
    new = num
    while new > 0:
        if new % 2 == 0:
            new /= 2
        else:
            new -= 1
        count += 1
    return count

print(numberOfSteps(num))

# REturn how many numbers are smaller in array than your number
nums = [1,2,3,5,1,7]
def smallerNumbersThanCurrent( nums):
    return [*map(sorted(nums).index, nums)]
print(smallerNumbersThanCurrent(nums))
