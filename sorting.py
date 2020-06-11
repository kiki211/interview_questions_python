# Sorting lists
li = [-2, 5,1,4,7,8,9,2,4,8,5,2,34,0,2,-23]
s_li = sorted(li, reverse=True)
s_li2 = sorted(li, key=abs)
print("List sorted\t", s_li)
print("List original\t", li)
print("List sorted with absolute value\t", s_li2)

li.sort() # changes the original li without creating new variable
print("List sorted by creating original variable\t", li)

# Tuple immutable
tup = (3,2,4,51,1,7)
s_tup = sorted(tup)
print("Tuple\t", s_tup)


# Dictonary
dic = {'d': 2, 'q': 1, 'a': 100, 'z': 1}
s_dic = sorted(dic)
print(s_dic)
print(dic)


# Quick sort
def quick_sort(a_list):
    if len(a_list) < 2:
        return a_list
    lesser = quick_sort([x for x in a_list[1:] if x <= a_list[0]])
    bigger = quick_sort([x for x in a_list[1:] if x > a_list[0]])
    return sum([lesser, [a_list[0]], bigger], [])

print("Quick sort:\t", quick_sort(li))

#---------------------------------------
# Selection Sort
#---------------------------------------
def selection_sort(A):
    for i in range(0, len(A) - 1):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]
    return A

print("Selection sort:\t", selection_sort(li))