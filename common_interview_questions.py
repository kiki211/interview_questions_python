# Balanced string
given_str = "{}hello World(I) am here (.to)help{.}.no4(6)y[u]b46"
opened = ['{', '[', '(']
closed = ['}', ']', ')']

def balanced_str(given_str):
    stack = []
    for i in given_str:
        if i in opened:
            stack.append(i)
        elif i in closed:
            ind = closed.index(i)
            if len(stack) > 0 and opened[ind] == stack[(len(stack)-1)]:
                stack.pop()
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


print(balanced_str(given_str))


# Get rid of extra spaces
in_str = "   Hello    my name is    Peter.      "
def get_rid_of_spaces(in_str):
    words_list = in_str.split()
    return " ".join(words_list)

print(get_rid_of_spaces(in_str))

# How many times number repreats in a string

in_str = "gsdg212fdsf122dsfsdf12dsfd12" # answer 4
target = '12'
def count_numbers_repeat(in_str, target):
    return len(in_str.split(target))-1

print(count_numbers_repeat(in_str, target))

# Are the words anagram?
word_a = "miam1"
word_b = "mamii"
def check_anagram(w1,w2):
    if len(w1) == len(w2):
        if sorted(w1) == sorted(w2):
            return "Words are anagram"
    return "Not anagram"

print(check_anagram(word_a, word_b))


# Sort a list
list_a = [3,1,4,9]
def sort_me(list_a):
    for i in range(len(list_a)-1, 0, -1):
        for j in range(i):
            if list_a[j] > list_a[j+1]:
                list_a[j],list_a[j+1] = list_a[j+1], list_a[j]
    return list_a
       
print(sort_me(list_a))

# Polendrome
word = "kayaks"
def check_polin(word):
    if word == word[::-1]:
        return "Word is a polindrome"

print(check_polin(word))


# Count how many pairs in a list
in_list = [1, 1, 1, 2, 2, 2, 1, 3, 4, 5, 6, 6]  # answer 3
# Easy solution
unique_list = []
counter = 0
for i in in_list:
    if i in unique_list:
        counter += 1
    else:
        unique_list.append(i)
print(counter)

# harder solution
count_words = {}
for i in in_list:
    if i not in count_words:
        count_words[i] = 1
    else:
        count_words[i] += 1
print(count_words)
sorted_dic = sorted(count_words.values(), reverse=True)[0:3] # return top 3
print(sorted_dic)

pair_number = 0
for k,v in count_words.items():
    pair_div = v//2
    if pair_div >= 1:
        pair_number += pair_div
print(pair_number)


