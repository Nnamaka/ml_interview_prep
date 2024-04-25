
"""
find the mid of the list of numbers.

if mid is query:
    check if it has duplicates on both sides:
        if it does:
            find the first and ending positions( count the duplicates)
        
        return the index of the query

else find mid: ( check if mid value is higher or lower than query)
"""

def binary_search (num, query):
    mid_point = len(num) - 1 // 2

    st = 0
    end = len(num) -  1
    if num[mid_point] == query:
        return first_and_end_pos(num,st, end=end, query=query)
    pass

def first_and_end_pos(numbers, start, end, query):
    count = 1

    
    pass

four = 1
show = 1 + max(four, four)
print(show)