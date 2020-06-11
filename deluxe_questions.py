# 1  Sum of two

# 2 Polindrome

# 3 Anagram

# 4 How many pairs in a string
one_str = "12345123459087" # 5
def pairs(one_str):
    pairs = 0
    bunker = []
    for i in one_str:
        if i in bunker:
            bunker.remove(i)
            pairs += 1
        else:
            bunker.append(i)
    return pairs


print(f"{pairs(one_str)} pairs.")





# 5 return only unique values and the number of unique values


# 6 Sort only odd numbers

# 7 Sort a list in O log n

# 8 Return a string and make letter capital if it follows _ or -.

# 9 How many 21 in string?
my_str = "21asfdsf21221fdsfdsfdsfs21" # answer: 4
def twenty_1(my_str):
    return len(my_str.split('21')) - 1


print(f"21 repeats {twenty_1(my_str)} times in given string.")


