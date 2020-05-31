#1 How many 12 in str?

in_str = "12jlkjlkjkl1212jlkjkl12jlk" # answer 4

def how_many12(in_str):
    answer = len(in_str.split('12')) -1
    return answer

print(how_many12(in_str))

print('--#--#--'*10)


#2 Change next letter if it follows _ to a capital. Make fist letter small.
import re
in_str = "Hello_my_name-is_John."


def capitalize_letter_after_(in_str):
    result = [w.capitalize() for w in in_str.split("_")]
    result[0] = result[0].lower()
    return "_".join(result)


print(capitalize_letter_after_(in_str))

print(re.split("_|-", in_str))

print('--#--#--'*10)

def polindrome(word):
    if word == word[::-1]:
        return "The {} is a polindrome.".format(word)
    return f"The {word} is not a polindrome."


a = "kayak"
print(polindrome(a))


def anagram(word, word2):
    if len(word) == len(word2):
        if sorted(word) == sorted(word2):
            return f"Words {word} and {word2} are anagrams."
    else:
        return False


a = "saa"
b = "sasa"
print(anagram(a, b))

listt = [x for x in range(0,20,2)] + [2,3,2,1,2,1,4]
def unique(listt):
    unique = []
    for num in listt:
        if num not in unique:
            unique.append(num)
        elif num in unique:
            unique.remove(num)
    return unique


print(unique(listt))


def fizzbuzz(x):
    for n in range(x):
        if n % 5 == 0 and n % 3 == 0:
            print("Fizzbuzz")
        elif n % 5 == 0:
            print("Fizz")
        elif n % 3 == 0:
            print("Buzz")
        else:
            print(n)


print(fizzbuzz(100))

def fibbonachi(x,y):
    a, b = 0, 1
    for i in range(x, y):
        print(a)
        a, b = b, a+b

fibbonachi(0, 10)


mu = [0, 1,1,1, 2,2, 3,3,3,3,3,3, 4, 5, 6, 7, 8, 9, 10] # 3,1,2

def top_common(mu):
    nums_dict = {}
    for i in mu:
        if i not in nums_dict:
            nums_dict[i] = 1
        else:
            nums_dict[i] += 1
    print(nums_dict)
    return sorted(nums_dict, key=nums_dict.get, reverse=True)[:3]


print(top_common(mu))


def how_many_pairs(listt):
    pairs = 0
    uniques = []
    for num in listt:
        if num in uniques:
            pairs += 1
            uniques.remove(num)
        else:
            uniques.append(num)
    return pairs


listt = [1,1,1,2,2,3,4,5]   # 2 pairs
print(how_many_pairs(listt))

squares = [x**x for x in range(1, 20) if x % 2 == 0]
print(squares)


def sorting(listt):
    pass

def balanced_string():
    pass


def sum_of_unique(listt):
    summ = 0
    quantity = 0
    uniques = set(listt)
    for num in uniques:
        summ += num
        quantity += 1
    return f"The sum of uniques numbers is {summ} and {uniques} unique numbers in the list."


listt = [x for x in range(20)] + [1,2,3,4,5]
print(sum_of_unique(listt))    #?????????????



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


chars = "abcdefghijklmnopqrstuvwxyz"
check_string = "i am checking this string to see how many times each character appears"

for char in chars:
    counter = check_string.count(char)
    if counter > 1:
        print(f"{char}: {counter}")

# map, zip    ??????????????????
print(list(map(lambda x: x**2, [3,2,4])))


def char_how_many_times(strin, target):
    return len(strin.split(target)) - 1

print(char_how_many_times("sisorisnisosi", 'si'))


# Balanced string
given_str = "{} Hello [dfdf] (here ), to help[p]."


def balanced_str(given_str):
    opened = ["[", "(", "{"]
    closed = ["]", ")", "}"]
    stack = []
    for i in given_str:
        if i in opened:
            stack.append(i)
        elif i in closed:
            ind = closed.index(i)
            if len(stack) > 0 and opened[ind] == stack[len(stack) -1]:
                stack.pop()
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


print(balanced_str(given_str))


# sort func
def sortt(listt):
    for n in range(len(listt)-1, 0, -1):
        for inner in range(n):
            if listt[inner] > listt[inner+1]:
                listt[inner],listt[inner+1] = listt[inner+1], listt[inner]

    return listt
listt = [3,2,5,2,9,4]
print(sortt(listt))

def get_rid_extra_spaces(strin):
    word_list = strin.upper().split()
    print(word_list)
    return " ".join(word_list)

strin = "   Hello,    world I am    here to      help!     "
print(get_rid_extra_spaces(strin))


# Apple Watch interview. Given a CSV file with the data.
# If the game was longer than blah time, find out who won and print out the team if it was a hame game for the winningteam.
file = "Home Team,Away Team,Start Time,End Time,Home Score,Away Score\nGiants,Athletics,638988124,639009724,3,0\nYankees,Red Socks,640651324,640654924,5,2\nAstros,White Socks,672180124,672187324,1,4\nDodgers,Padres,677458504,677458624,12,9\nRockies,Marlins,674780224,674783944,8,9\nBlue Jays,Cardinals,674575144,674600344,7,15\nBlue Jays,Cardinals,674600344,7,15"

data = file.split('\n')
for line in data[1::]:
    line = line.strip(" ").split(",")
    if len(line) == 6:
        end_time = line[3]
        start_time = line[2]
        if int(end_time) - int(start_time) > 90*60:
            if int(line[-1]) > int(line[-2]):
                print(line[1])
            else:
                print(line[0])







