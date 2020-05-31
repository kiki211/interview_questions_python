
l = ["koko", "hi", "hey", "bye", "koko"]
def get_uniqe_items(l):
    uniqe = []
    for i in l:
        if i in uniqe:
            uniqe.remove(i)
        else:
            uniqe.append(i)
    return uniqe

print(get_uniqe_items(l))

def count_words(listt):
    result = {}
    for i in listt:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

print(count_words(l))




