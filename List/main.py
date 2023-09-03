my_list=["apple","banana","cherry"]

"""
list items are ordered ,changable and allow duplicate values
list items are indexed , the first item has index[0], the second item has index[1] etc 
"""
print(my_list)

"""
when we say that list are orderd , it means that the items have a defined order , and that order will not change 
#  if iam placing new list on the list , the new list will be placed at the end of the llist 

"""


second_list=['apple','banana','cherry','apple']
print(second_list,"second list::")
"""it allow duplicate data """


# list length 
print("length of first list::",len(my_list))

"""list items-- data types"""

list1=["apple","banana","cherry"]
list2=[1,2,3,4,5,6]
list3=[True,False,True]


list4=["abc",34,True,40,'male']
print(list4)
print(type(list4))


# the list() constrauctor 

# it is also possibel to use the list() contractor when we creating  a new list 

this_list=list(("apple","banana","cherry"))
print(type(this_list))
print(this_list)