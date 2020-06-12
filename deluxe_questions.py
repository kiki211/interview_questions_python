# 1  Sum of two

# 2 Polindrome
in_str = 'kayak'


def palindrome(in_str):
    if in_str == in_str[::-1]:
        return True


print(palindrome(in_str))


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

# 6 Sort odd numbers only
my_list = [7, 2, 1, 4, 11, 9, 2]  # answer: [1, 2, 7, 4, 9, 11, 2]


def sort_odds(input_list):
    odd_nums = sorted([n for n in input_list if n % 2 != 0])
    count = 0
    for i in range(len(input_list)):
        if input_list[i] % 2 != 0:
            input_list[i] = odd_nums[count]
            count += 1
    return input_list


print(sort_odds(my_list))

# 7 Sort a list in O log n

# 8 Return a string and make letter capital if it follows _ or -.
sentence = "Hello_my-name_is-Unknown."  #  answer: Hello_My-Name_Is-Unknown.


def capitalize_word(sentence):
    new_sentence = []
    patterns = ["_", "-"]
    for l in sentence:
        if len(new_sentence) > 0 and new_sentence[-1] in patterns:
            new_sentence.append(l.upper())
        else:
            new_sentence.append(l)
    return ''.join(new_sentence)


print(f"Returning capitalized word following after - and _ here: {capitalize_word(sentence)}")


# 9 How many 21 in string?
my_str = "21asfdsf21221fdsfdsfdsfs21" # answer: 4


def twenty_1(my_str):
    return len(my_str.split('21')) - 1


print(f"21 repeats {twenty_1(my_str)} times in given string.")


