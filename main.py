#making a Dictionary
#Dictornary is a collection of items in a key value pair similar to list but without index numbers

person= {'name' : 'sanjana' , 'age' : 26 , 'hobby': 'Watching movies'} 
print(person)

#Acess the values using keys
print(person['name']) 

print(person['hobby']) 

#adding new item to the dictionary
person['country'] = 'England' #country is a key and England is a value for it
print(person)

#Getting keys from dictoinary
print(person.keys())

#Getting values
print(person.values())

#size / length of dictionary - how many items in dictionary

print(len(person))

#check wheter key exists in the dictionary 
print('hobby' in person)#this will give True if there otherwise False

#Deleting key-value pair (item) from the dictionary 
del person['hobby']
print(person)

#modifying values of the dictionary 
person['age']=24
print(person)

#Ieratating (going to each item) in the dictionary
list=[]#empty list to store the values
for i in person:
    list.append(i) #appendis used to add an item to the list

print(list)

#sorting items in the list
print(list.sort())

#making a Dictionary
#Dictornary is a collection of items in a key value pair similar to list but without index numbers

Game= {'Game 1 ' : 'Fortnite' , 'Game 2' : 'minecraft' , 'Game 3 ': 'Call of Duty'} 
print(Game)

#adding new item to the dictionary
Game['Game 4'] = 'Volleyball' #Game 4  is a key and Volleyball is a value for it
print(Game)



