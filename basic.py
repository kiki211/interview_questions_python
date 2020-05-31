# # Polindrome
# word = "kayak"
# def check_polindrome(word):
#     if word == word[::-1]:
#         return "It's a polindrome"
#
#
# def rev(word):
#     return word[::-1]
#
#
# def check_recurs(word):
#     rever = rev(word)
#
#     if rever == word:
#         return "Yes"

#
# print(check_polindrome(word))
# print(check_recurs(word))


# Iterative method

# function to check string is
# palindrome or not
# str = "kayaks"
# def isPalindrome(str):
#     # Run loop from 0 to len/2
#     for i in range(0, int(len(str)/2)):
#         if str[i] != str[len(str) - i - 1]:
#             return False
#     return True
#
#
# # main function
# s = "malayalam"
# ans = isPalindrome(s)
#
# if (ans):
#     print("Yes")
# else:
#     print("No")



# a="pythontutorial"
# print('%. 6s' % a)  ?????

# f = open("softwaretestinghelp.txt", "r")
# print(f.read(10))
# print(f.read())


# str_1 = "Python Language"
# print(str_1[4:])
# print(str_1[:5])
# print(str_1[0:-1:2])
# print(str_1[::-1])
# print(str_1[:6] + str_1[6:])
#
# import time
# currenttime= time.localtime(time.time())
# print ("Current time is", currenttime)
#
#
# # All dict keys
# dict = {"a":1, "b":2, "c":3, "b":5}
# print(dict.keys())

# for var in list(range(1, 11, 2)):
#     print(var)
# result = []
# for k, i in dict.items():
#     if k not in result:
#         result.append(k)
# print(result)

# final = {}
# for k, i in dict.items():
#     if k in final.keys():
#         final[k] += 1
#     else:
#         final[k] = 1
# print(final) # how to count how many times key repeats in dict?
#
#
# aray = [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6]
# aray.pop()
# print(aray)
# aray.remove(3.7)
# print(aray)
# aray.append(99)
# print(aray)
# aray.extend([11,12,13])
# print(aray)
# aray.insert(1, 45)
# print(aray)
# strin = "hello world"
# print(strin.upper())
# print(strin.capitalize())
# print(strin.title())
# print(strin.split('w')) # returns list
# print(strin.find('l'))
# print(strin.lower())
# print(strin.isalpha())
# print(strin.replace("l", "$", 2))
# print(len(strin))
# print(strin.isalnum())
# print(strin.islower())
#
# from random import shuffle
# x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
# shuffle(x)
# print(x)

# Sort buble
n = [6, 5, 4, 3, 2, 1, 0]
for x in range(len(n)-1, 0, -1):
    for i in range(x):
        if n[i] > n[i+1]:
            n[i], n[i+1] = n[i+1], n[i]
print(n)

########################################################
######### TOP 10 JAVA SELENIUM QUESTIONS ###############
########################################################

#1 Filter duplicates
l = [6, 5,3, 4, 3, 2, 2, 1, 0]
print(set(l)) # return all without repeated ones
def return_unique(list1): # returns only unique
    answer = []
    for el in l:
        if el in answer:
            answer.remove(el)
        else:
            answer.append(el)
    return answer

print(return_unique(l))

#2 Reverse a number
n = 12345
new = str(n)
print(int((new)[::-1]))

# Get rid of multiple spaces
example = " Hey dude     I    am here.   "
print(example.strip(" "))
res = " ".join(example.split())
print(res)

create_sent = ["Hello", "We", "are", "here", "to", "help", "!"]
print(create_sent)
new = " ".join(create_sent)
print(new)


# Write Java code to swap two numbers without using a temporary variable?
a = 3
b = 1
a, b = b, a
print(a, b)

c = b
b = a
a = c
print(a, b)

# Write a Java program to find the longest substring from a given
# string which doesn’t contain any duplicate characters?

# Count how many times each item is repeated
items = ["2", "2", "hello", "bye", "hello", "2"]
res = {}
def count_words(items):
    for i in items:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res

print(count_words(items))

# How many times given number is repeated in str?
strin = "21232221"
def rep_num(trin, given_num):
    return len(strin.split(given_num)) -1

print(rep_num(strin, '21'))

# If anagram
w1 = "listen"
w2 = "silent"
if sorted(w1) == sorted(w2):
    print("True, it's an anagram")
else:
    print("Not an anagram")

# Modulo
# Lambda
# ZIP, MAP, Enumerate
print(dict(zip(['a', 'b'],[1,2])))
a = map(['a', 'b'],[1,2])
print(a)

x = 121
x = str(x)
if x == x[::-1]:
    print("True")


print(float(3))

word = "kayaks"
def palindrome(word):
    if word == word[::-1]:
        return f"The word {word} is a palindrome."
    return False

print(palindrome(word))

listt = [x**2 for x in range(20)] + [0,1,4,9,16,25,36,47,64,81]
def no_repetition(listt):
    return set(listt)

print(no_repetition(listt))

listt = [10,10,10]
def index_each_item(listt):
    for idx, i in enumerate(listt):
        print(i, idx)

print(index_each_item(listt))


def how_many_instr(strr, condition):
    return len(strr.split(condition)) - 1


strr = "aloha"
print(how_many_instr(strr, 'a'))


def fizzbuzz(x):
    for i in range(x):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Fizz")
        elif i % 3 == 0:
            print("Buzz")
        else:
            print(i)

print(fizzbuzz(100))




a = [3,6,4,5,3,2,1,2]
b = 9
def twoSum(nums, target):
    result = {}
    for n in nums:
        for each in nums:
            if nums[each] == target - nums[n]:
                result[nums[n]] = nums[each]
    return result


print(twoSum(a, b))



# Practice
def if_letterafer_A(in_str):
    result = []
    for i in in_str:
        if i == '_' and in_str[i+1].isalnum():
            in_str[i + 1].upper()
        result.append(i)
    return result

print(if_letterafer_A("adfs_dfdaf_adfds_d."))
