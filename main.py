import random
#import my_module
#random_intvar   = random.randint(1,5)
#random_floatvar = random.random()

#print(f"Random Int Value is : {random_intvar}")
#print(f"Random Int Value is : {random_floatvar}")
#print(my_module.pi)

family_members = ["Ravi", "Astha","Illisha","Lika"]
print(family_members)
print(family_members[0]+ " Dubey")
family_members[3] = 'Liku' #change the value in the list at given position
print(family_members)
family_members.append('Liki') #append the element at last
print(family_members)
family_members.insert(2,"Dolu") #insert the element in the list at a particular position
print(family_members)
family_members.count("Liku")
lika_count = family_members.count("Liku") #count occurrence of the element  in the list
print(lika_count)
family_members.reverse() #it reverses the string
print(family_members)
index= family_members.index("Astha") #gives the element occurrence in the list
print(index)
family_members.sort() #sort the element alphabetically
print(family_members)
family_members.pop() #removes last element from the list
print(family_members)
family_members.pop()
print(family_members)
total_names= len(family_members)
print(total_names)


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
total_names= len(names)
print(total_names)
random_number = random.randint(0,total_names-1)
print(random_number)
print(f"{names[random_number]} is going to buy the meal today")