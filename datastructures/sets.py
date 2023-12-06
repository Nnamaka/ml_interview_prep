Days = {'mon','tue','wed','thurs','fri','sat','sun'}
Months = set(['Jan','Feb','Mar'])

# # adding elements
# Days.add('mad')
# print(Days)

# # remove element
# Months.discard('Jan')
# print(Months)

# union of sets
# DaysA = set(["Mon","Tue","Wed"])
# DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
# AllDays = DaysA|DaysB
# print('union of DaysA and DaysB',AllDays)

#instersection
# DaysA = set(["Mon","Tue","Wed"])
# DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
# AllDays = DaysA & DaysB
# print(AllDays)

#Difference - the difference operation on two sets produces a new
#set containing only the elements from the first set and none from the
#second set
# DaysA = set(["Mon","Tue","Wed"])
# DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
# AllDays = DaysA - DaysB
# print(AllDays)

#Compare Sets - we can check if a given set is a subset or superset of 
#another set
# DaysA = set(["Mon","Tue","Wed"])
# DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
# SubsetRes = DaysA <= DaysB
# SupersetRes = DaysB >= DaysA
# print(SubsetRes)
# print(SupersetRes)