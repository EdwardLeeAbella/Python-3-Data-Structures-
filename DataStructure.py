# PYTHON DATA STRUCTURE

# LIST = a collection of elements in order list = []
# list is can be iterate using loops
# list can be slicce using [:]
list1 = [1, 2, 3]
#example of a list containing 3 integers
list2 = [1, "string", 4.3, True, [10, 20]]
# example of a with different elements
print(list2)
#printing out list2
print(list1[0]) or print(list1[-1])
# printing out index 0 of the list 1 = 1 , prints out 3
print(list1[:2])  or print(list1[0:2:2]) #stride
#print out elements from 0 index up to 1 but not 2
list2.append("edward")
#adding an element in the end of list2
list2.insert(2, "False")
#adding an element with the index 2 on the list2
list2.remove("string")
#remove string in list2
list2.reverse()
#reverse the list order or flip
list2.sort()
# sort the list in accending order

# TUPLE = is a list with constraint
# collection of the in ordered elements (immutable) cant be change
credit_card = (1316567892, 'Edward Lee', 11/20, 0123)
print(credit_card)
#prints out the tuple credit_card
person = ("Maegan", 22, 'barbeque')
name, age, favfood = person
print(name)
print(age)
print(favfood)
# upacked tuple name person
person1 = ("Maegan", 22, 'barbeque')
person2 = ("Edward", 22, 'Fried Chicken')
people = [person1, person2]

for name, age, favfood in people:
    print(name)
    print(age)
    print(favfood)
    print()
# unpack tuples using for loops

#SETS = is like a list or a tuple but not ordered
# cannot have a duplicate set1 = {}
set1 = {1,2,3,4,5,6}
set1.add(1)
set1.add(6)
print(set1)
#print out set1
#set can be casted into a list and vice versa
list3 = [1,1,2,2,3,3,4,5,6,6]
#list of integers with duplicate
no_dup_set = set(list3)
#convert list to a set
no_dup_list = list(no_dup_set)
#then set to list to get rid of duplicate
print(no_dup_list)
#print out the new list without duplicates
library1 = {'harry potter', 'lord of the rings'}
library2 = {'harry potter', 'star wars'}
#2 diff set
town_lib = library1.union(library2)
#concatinate both lib1 and lib2 to a new set town_lib
print(town_lib)
#print out town_lib
# intersection and difference is another function in set


#HASH TABLE IN PYTHON = DICTIONARY OR DICT
#contains a key and a value or in other words an input/output pair
# can name your own index
#very structured data holder
groceries = {
    'banana': [5, "ripe : 3", "unripe : 2"],
    'oranges': [5, "ripe : 3", "unripe : 2"]
}
#create a dict groceries with index banana and oranges
print(groceries['banana'])
#print out the value of banana index
#dict.items() is = a list of tuples with key value pair
#dict.keys() is = a list of keys
#dict.values() is = a list of values

# Unpack dict()
post = {'user_id': 209, 'message': 'pretty', 'language': 'english'}
#unpack dict
for key in post.keys():
    value = post[key]
    print(key, "=", value)

#another way to unpack dict
c = {}
c["edward"] = 25
c["maegan"] = 23
for key, value in c.items():
    print("Key: ")
    print(key)
    print("Value: ")
    print(value)
    print()



















